import datetime
import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_google_calendar():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('calendar', 'v3', credentials=creds)

def create_event(service, task_name, start_time, end_time, date):
    # Handle midnight transitions
    if end_time < start_time:
        end_date = (datetime.datetime.strptime(date, "%Y-%m-%d") + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    else:
        end_date = date

    event = {
        'summary': task_name,
        'start': {
            'dateTime': f"{date}T{start_time}:00",
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': f"{end_date}T{end_time}:00",
            'timeZone': 'Asia/Kolkata',
        },
    }
    
    try:
        event = service.events().insert(calendarId='primary', body=event).execute()
        print(f"Event created: {event.get('htmlLink')}")
    except Exception as e:
        print(f"An error occurred: {e}")

def generate_dates_for_rotation(start_date, num_days):
    dates = []
    current_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
    for _ in range(num_days):
        dates.append(current_date.strftime("%Y-%m-%d"))
        current_date += datetime.timedelta(days=1)
    return dates

def main():
    service = authenticate_google_calendar()

    tasks = [
        # list of tasks in the format (task_name, start_time, end_time)
    ]

    num_days = 7
    start_date = "2024-09-06"

    dates = generate_dates_for_rotation(start_date, num_days)

    for i, date in enumerate(dates):
        rotated_tasks = tasks[i % len(tasks):] + tasks[:i % len(tasks)]
        for task_name, start_time, end_time in rotated_tasks:
            create_event(service, task_name, start_time, end_time, date)

if __name__ == '__main__':
    main()
