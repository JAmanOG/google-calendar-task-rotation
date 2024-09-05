# Google Calendar Task Rotation

This project automates the rotation of tasks in your Google Calendar. It schedules different tasks to be performed on different days of the week and updates your Google Calendar with these events.

## Features

- Rotates tasks every 7 days
- Integrates with Google Calendar API
- Automates task scheduling

## Prerequisites

Before running the script, ensure you have the following:

- Python 3.x
- Virtual environment
- Google Cloud Platform project with Calendar API enabled
- OAuth 2.0 credentials

## Setup

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/JAmanOG/Adding-rotational-Task-to-GoogleCalender
cd Adding-rotational-Task-to-GoogleCalender
```

### 2. Create a Virtual Environment

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install Dependencies
Install the required Python packages:

```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

### 4. Obtain OAuth 2.0 Credentials
- Go to the Google Cloud Console.
- Create a new project or select an existing project.
- Enable the Google Calendar API.
- Create OAuth 2.0 credentials and download the credentials.json file.
- Place the credentials.json file in the project directory.

### 5. Configure the Script
- Open rotate_task.py.
- Adjust the tasks list and start_date as needed.

### 6. Run the Script
Run the script to create events in your Google Calendar:
```bash
python rotate_task.py
```

### 7. Automate Script Execution
To run the script automatically every 7 days, set up a cron job (Linux/macOS) or a Task Scheduler task (Windows):
Setting Up a Cron Job (Linux/macOS)

#### 1. Open crontab:

```bash
crontab -e
```

#### 2. Add the following line to run the script every Sunday at 1 AM:

```bash
0 1 * * 0 /path/to/your/venv/bin/python /path/to/your/rotate_task.py
```
#### 3. Save and exit.

### Setting Up Task Scheduler (Windows)
1. Open Task Scheduler.
2. Create a new basic task.
3. Set the trigger to run weekly.
4. Set the action to start a program, and specify the path to Python and the script.
5. Save the task.

## Contributing
Feel free to open issues or submit pull requests. Contributions are welcome!

## License
This project is licensed under the MIT License.
