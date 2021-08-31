# Script configurations
START = "10:00"  # Work start time ("HH:MM")
END = "18:00"  # Work end time   ("HH:MM")
DAYS_TO_GET_AVAILABILITY_FOR = 5  # The number of dates to consider for availability
INITIAL_MESSAGE = "Here is my availability for the next 5 work days"

# Google API constants
TOKEN_JSON = "certs/token.json"  # Token JSON path
CERTS_JSON = "certs/certs.json"  # Credentials path
MAX_EVENTS_TO_FETCH = 100

# Scopes determine what the API service will be allowed to do.
# Since we only need to read the calendar, readonly is the scope with the least permissions needed
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
