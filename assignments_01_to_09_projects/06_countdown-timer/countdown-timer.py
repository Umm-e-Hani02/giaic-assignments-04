import time

def countdown_timer(minutes, seconds):
    total_seconds = minutes * 60 + seconds

    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        timer_display = f"{mins:02d}:{secs:02d}"
        print(timer_display, end="\r")
        time.sleep(1)
        total_seconds -= 1

    print("⏰ Time's up!")

# User input for time
print("Welcome to the Countdown Timer!")
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

countdown_timer(minutes, seconds)
