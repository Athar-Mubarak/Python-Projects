import os
from datetime import datetime
from playsound import playsound
import time

# Get input and provide a clear example
print("Format: HH:MM:SS AM/PM (Example: 08:30:00 PM)")
alarm_time = input("Enter the alarm time: ").strip()

try:
    # Splitting by spaces and colons is safer than hard-coded slicing
    # Example input: "08:30:00 PM"
    time_parts = alarm_time.split(" ")
    hms = time_parts[0].split(":")

    alarm_hour = hms[0]
    alarm_minute = hms[1]
    alarm_second = hms[2]
    alarm_period = time_parts[1].upper()

    print(f"Alarm set for {alarm_hour}:{alarm_minute}:{alarm_second} {alarm_period}...")

    while True:
        now = datetime.now()

        # Checking against current time
        if (alarm_hour == now.strftime("%I") and
                alarm_minute == now.strftime("%M") and
                alarm_second == now.strftime("%S") and
                alarm_period == now.strftime("%p")):
            print("\nWake up!")
            playsound('audio.mp3')
            break

        # Sleep for 0.1 seconds to save CPU, but stay fast enough to catch the second
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nAlarm cancelled.")
except Exception as e:
    print(f"Error: Make sure you entered the time correctly! ({e})")