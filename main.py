from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import config
import constants.constants as constants
from utils.time_utils import get_next_x_work_dates, convert_time_string_to_id, convert_id_to_time_string
from datetime import datetime

# TODO:
# 1. Authenticate with OAuth instead (for easier configuration)
# 2. Make this into a Chrome extension

# Read credentials from local JSON and return the Google Calendar API service
def get_api_service():
    creds = None
    if os.path.exists(config.TOKEN_JSON):
        creds = Credentials.from_authorized_user_file(config.TOKEN_JSON, config.SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                config.CERTS_JSON, config.SCOPES)
            creds = flow.run_local_server(port=0)

        with open(config.TOKEN_JSON, 'w') as token:
            token.write(creds.to_json())  # Cache credentials

    return build('calendar', 'v3', credentials=creds)


# Calls Calendar API and returns list of events in calendar
def get_events(service):
    events_result = service.events().list(
        calendarId='primary',
        timeMin=datetime.utcnow().isoformat() + 'Z',
        maxResults=config.MAX_EVENTS_TO_FETCH,
        singleEvents=True,
        orderBy=constants.EVENT_START_TIME_ORDERBY) \
        .execute()
    events = events_result.get('items', [])

    return events


def get_events_by_date_dictionary(events):
    events_by_date = {}

    for event in events:
        event_start_split = str(event[constants.EVENT_START].get(constants.EVENT_DATETIME)).split("T")
        event_end_split = str(event[constants.EVENT_END].get(constants.EVENT_DATETIME)).split("T")

        date = event_start_split[0]

        if date not in events_by_date.keys():
            events_by_date[date] = []

        start_time = event_start_split[1][0:8]
        end_time = event_end_split[1][0:8]

        events_by_date[date].append([start_time, end_time])

    return events_by_date


def main():
    events = get_events(get_api_service())
    events_by_date = get_events_by_date_dictionary(events)
    next_five_work_dates = get_next_x_work_dates(config.DAYS_TO_GET_AVAILABILITY_FOR)

    result = config.INITIAL_MESSAGE + ":\n"
    for date in next_five_work_dates:

        if date not in events_by_date.keys():
            events_by_date[date] = []

        result += date + ": "
        availability = [constants.AVAILABLE for x in range(0, 96)]

        # Mark time before START and after END as unavailable
        for x in range(0, convert_time_string_to_id(config.START)):
            availability[x] = constants.UNAVAILABLE
        for y in range(convert_time_string_to_id(config.END), 96):
            availability[y] = constants.UNAVAILABLE

        # Mark appointments as unavailable
        for appointment in events_by_date[date]:
            for x in range(convert_time_string_to_id(appointment[0]),
                           convert_time_string_to_id(appointment[1])):
                availability[x] = constants.UNAVAILABLE

        # Construct times available string
        calculating_availability = False
        first_available_time, second_available_time = "", ""
        for x in range(0, 96):
            if availability[x] == constants.AVAILABLE:
                if not calculating_availability:
                    first_available_time = convert_id_to_time_string(x)
                    calculating_availability = True

            if availability[x] == constants.UNAVAILABLE:
                if calculating_availability:
                    second_available_time = convert_id_to_time_string(x)
                    calculating_availability = False
                    result += first_available_time + config.TIME_ZONE_STR + " - " + second_available_time + \
                              config.TIME_ZONE_STR + ", "

        result = result[:-2] + "\n"  # Remove trailing comma and go to new line

    print(result)


if __name__ == '__main__':
    main()
