# Scopes determine what the API service will be allowed to do.
# Since we only need to read the calendar, readonly is the scope with the least permissions needed
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

### Local constants for script ###
START = "10:00"                 # Work start time ("HH:MM")
END = "18:00"                   # Work end time   ("HH:MM")
AVAILABLE = "Available"         # Constant for availability in time period
UNAVAILABLE = "Unavailable"     # Constant for not being available in time period
TIME_ZONE_STR = "EST"           # Not used for anything logical, this can be anything


### Google API constants ###
TOKEN_JSON = "token.json"       # Token JSON file name
CERTS_JSON = "certs.json"       # Credentials JSON file name

EVENT_START = "start"
EVENT_END = "end"
EVENT_DATETIME = "dateTime"

EVENT_START_TIME_ORDERBY = "startTime"
