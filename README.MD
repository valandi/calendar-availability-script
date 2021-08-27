# Calendar Availability

## Usage

### Get your credentials from Google
1. Create a new project (it doesn't matter what you name it, we just need the credentials)
1. Navigate to https://console.cloud.google.com/apis/credentials
1. Click on "+ CREATE CREDENTIALS"
1. Choose "Oauth Client ID"
1. Choose "Application type" "Desktop App"
1. Click "CREATE"
1. Under "Actions", click the arrow to download your credentials
1. Place credentials in same directory as "main.py" and save as certs.json. 

### Use the script
1. Clone the repo:
``` git clone ```
1. cd into project directory
``` cd calendar-availability-script ```
1. Run the script
``` python3 /path/to/main.py ```
1. As long as your credentials are set up correctly, you should see a neatly formatted availability for the next 5 work days!


