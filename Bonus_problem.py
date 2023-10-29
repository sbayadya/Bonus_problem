import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat)  # Print countdown line on a new line
        time.sleep(1)  # Wait for 1 second
        seconds -= 1
    print("Time's up!")

user_input = input("Enter the time in seconds: ")
try:
    countdown = int(user_input)
    countdown_timer(countdown)
except ValueError:
    print("Invalid input. Please enter a valid number of seconds.")

