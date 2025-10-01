import datetime
import os
import pickle
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_google_calendar():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('calendar', 'v3', credentials=creds)
    return service

def create_event(service, summary, start_date, start_time, end_time, recurrence, calendar_id):
    start_datetime = f'{start_date}T{start_time}:00'
    end_datetime = f'{start_date}T{end_time}:00'
    
    event = {
        'summary': summary,
        'start': {
            'dateTime': start_datetime,
            'timeZone': 'America/New_York',  # Change to your timezone
        },
        'end': {
            'dateTime': end_datetime,
            'timeZone': 'America/New_York',  # Change to your timezone
        },
        'recurrence': recurrence,
    }

    event = service.events().insert(calendarId=calendar_id, body=event).execute()
    print(f'Event created: {event.get("htmlLink")}')

def main():
    service = authenticate_google_calendar()
    
    # User inputs
    calendar_id = input("Enter your Calendar ID: ")
    class_name = input("Enter the class name: ")
    days_input = input("Enter the days (e.g., MO,TU,WE): ")
    days = days_input.split(',')
    start_time = input("Enter the start time (HH:MM, 24-hour format): ")
    end_time = input("Enter the end time (HH:MM, 24-hour format): ")

    date_ranges = []
    while True:
        start_date = input("Enter the start date (YYYY-MM-DD) or 'done' to finish: ")
        if start_date.lower() == 'done':
            break
        end_date = input(f"Enter the end date (YYYY-MM-DD) for the range starting {start_date}: ")
        date_ranges.append((start_date, end_date))
    
    # Create events based on user inputs
    for start_date, end_date in date_ranges:
        create_event(
            service=service,
            summary=class_name,
            start_date=start_date,
            start_time=start_time,
            end_time=end_time,
            recurrence=[f'RRULE:FREQ=WEEKLY;BYDAY={",".join(days)};UNTIL={end_date.replace("-", "")}'],
            calendar_id=calendar_id
        )

if __name__ == '__main__':
    main()