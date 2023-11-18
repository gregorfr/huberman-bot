import random
from icalendar import Calendar, Event
from datetime import datetime, timedelta
import pytz

# Function to generate random protocol instructions
def generate_protocol(file_path):
    def generate_instruction():
        x = random.randint(1, 5)  # Random number between 1-5
        z = random.randint(1, 120)  # Random number between 1-120
        y = random.choice(["jumping jacks", "push-ups", "sit-ups", "squats", "lunges", "sunlight viewing", "doomscrolling"])  # Random activity
        return f"{x} times a week, for {z} minutes, do {y}"

    with open(file_path, 'w') as file:
        for _ in range(5):  # Generate 5 instructions for each protocol
            instruction = generate_instruction()
            file.write(instruction + '\n')

# Function to create iCal data
def create_ical(file_path):
    def create_event(day):
        event = Event()
        event.add('summary', 'Work')
        event.add('dtstart', day)
        event.add('dtend', day + timedelta(hours=8))
        event.add('dtstamp', datetime.now())
        return event

    cal = Calendar()
    cal.add('prodid', '-//Work Calendar//mxm.dk//')
    cal.add('version', '2.0')

    start_date = datetime.now().replace(hour=8, minute=0, second=0, microsecond=0)
    if start_date.weekday() != 0:
        start_date -= timedelta(days=start_date.weekday())

    num_weeks = 4
    for week in range(num_weeks):
        for day in range(5):
            event_day = start_date + timedelta(days=day + week * 7)
            event = create_event(event_day)
            cal.add_component(event)

    with open(file_path, 'wb') as f:
        f.write(cal.to_ical())
    print(f"iCal file created at {file_path}")

# User input for choice
choice = input("Enter '1' to generate iCal data or '2' to generate protocol instructions: ")

if choice == '1':
    ical_file_path = 'Data/work_schedule.ics'
    create_ical(ical_file_path)
elif choice == '2':
    num_protocols = 10

    for i in range(1, num_protocols + 1):
        protocol_file_path = f'Data/random_protocol{i}.txt'
        generate_protocol(protocol_file_path)
        print(f"Protocol instructions created at {protocol_file_path}")
else:
    print("Invalid choice. Please enter '1' or '2'.")
