from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from time_utils import *
from constants import *
from datetime import datetime


# Read credentials from local JSON and return the Google Calendar API service
def get_api_service():
    creds = None
    if os.path.exists(TOKEN_JSON):
        creds = Credentials.from_authorized_user_file(TOKEN_JSON, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CERTS_JSON, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(TOKEN_JSON, 'w') as token:
            token.write(creds.to_json())  # Cache credentials

    return build('calendar', 'v3', credentials=creds)


# Calls Calendar API and returns list of events in calendar
def get_events(service):
    events_result = service.events().list(
        calendarId='primary',
        timeMin=datetime.utcnow().isoformat() + 'Z',
        maxResults=100,
        singleEvents=True,
        orderBy=EVENT_START_TIME_ORDERBY) \
        .execute()
    events = events_result.get('items', [])

    return events


def get_events_by_date_dictionary(events):
    events_by_date = {}

    for event in events:
        date = str(event[EVENT_START].get(EVENT_DATETIME)).split("T")[0]

        if date not in events_by_date.keys():
            events_by_date[date] = []

        start_time = str(event[EVENT_START].get(EVENT_DATETIME)).split("T")[1][0:8]
        end_time = str(event[EVENT_END].get(EVENT_DATETIME)).split("T")[1][0:8]

        events_by_date[date].append([start_time, end_time])

    return events_by_date


def main():
    events = get_events(get_api_service())
    events_by_date = get_events_by_date_dictionary(events)
    next_five_work_dates = getNextFiveWorkDates()

    print("Here is my availability for the next 5 work days:")
    times_available = ""

    for date in next_five_work_dates:
        times_available += date + ": "
        availability = [AVAILABLE for x in range(0, 96)]

        # Mark time before START and after END as unavailable
        for x in range(0, convertTimeStringTo15MinuteId(START)):
            availability[x] = UNAVAILABLE
        for y in range(convertTimeStringTo15MinuteId(END), 96):
            availability[y] = UNAVAILABLE

        # Mark appointments as unavailable
        for appointment in events_by_date[date]:
            for x in range(convertTimeStringTo15MinuteId(appointment[0]),
                           convertTimeStringTo15MinuteId(appointment[1])):
                availability[x] = UNAVAILABLE

        # Construct times available string
        calculating_availability = False
        first_available_time, second_available_time = "", ""
        for x in range(0, 96):
            if availability[x] == AVAILABLE:
                if not calculating_availability:
                    first_available_time = convert15MinuteIdToTimeString(x)
                    calculating_availability = True

            if availability[x] == UNAVAILABLE:
                if calculating_availability:
                    second_available_time = convert15MinuteIdToTimeString(x)
                    calculating_availability = False
                    times_available += first_available_time + TIME_ZONE_STR + " - " + second_available_time + TIME_ZONE_STR + ", "

        times_available = times_available[:-2] + "\n"  # Remove trailing comma and go to new line

    print(times_available)


if __name__ == '__main__':
    main()
