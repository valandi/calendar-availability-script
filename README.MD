# Calendar Availability

## Pre-requisites 
1. Ensure that Python3 is installed on MAC (try ``` python3 -v ```)
https://docs.python-guide.org/starting/install3/osx/
2. Ensure that pip is installed (try ``` pip --version```)
https://pip.pypa.io/en/stable/installation/

## Usage
### Get your credentials from Google (Should take about 5 minutes)
1. Navigate to https://console.cloud.google.com/apis/credentials
1. Create a new project (it doesn't matter what you name it, we just need the credentials)
1. Click on "+ CREATE CREDENTIALS"
1. Choose "Oauth Client ID"
1. Choose "Application type" > "Desktop App"
1. Click "CREATE"
1. Under "Actions", click the arrow to download your credentials
1. Save your credentials as "certs.json" in the certs/ directory. (You can modify the path in config_variables.py if you want)

### Use the script
1. Clone the repo:
``` git clone https://github.com/valandi/calendar-availability-script.git```
2. cd into project directory
``` cd calendar-availability-script ```
3. Install requirements
``` pip install -r requirements.txt```
4. Modify config_variables.py as needed (you will want to modify START, END, and TIME_ZONE_STR in config_variables.py)
5. Run the script
``` python3 main.py ```
6. As long as your credentials are set up correctly, you should see a neatly formatted availability for the next 5 work days!

### Sample output

Here is my availability for the next 5 work days:\
2021-08-27: 10:00EST - 12:00EST, 17:00EST - 18:00EST\
2021-08-30: 10:00EST - 12:00EST, 13:00EST - 18:00EST\
2021-08-31: 10:00EST - 11:00EST, 11:45EST - 12:30EST, 13:00EST - 18:00EST\
2021-09-01: 11:00EST - 12:30EST, 13:00EST - 15:00EST, 16:00EST - 18:00EST\
2021-09-02: 10:00EST - 12:30EST, 13:00EST - 18:00EST

