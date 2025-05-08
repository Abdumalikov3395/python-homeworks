import datetime
import time
import re
from dateutil import parser
import pytz

def age_calculator():
    birth_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.datetime.strptime(birth_str, "%Y-%m-%d").date()
    today = datetime.date.today()

    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    if days < 0:
        months -= 1
        days += (birthdate.replace(month=birthdate.month + 1) - birthdate).days

    if months < 0:
        years -= 1
        months += 12

    print(f"Your age: {years} years, {months} months, and {days} days.")

def days_until_next_birthday():
    birth_str = input("Enter your birthdate (YYYY-MM-DD): ")
    birthdate = datetime.datetime.strptime(birth_str, "%Y-%m-%d").date()
    today = datetime.date.today()
    next_birthday = birthdate.replace(year=today.year)

    if next_birthday < today:
        next_birthday = next_birthday.replace(year=today.year + 1)

    delta = next_birthday - today
    print(f"Days until your next birthday: {delta.days}")

def meeting_scheduler():
    now_str = input("Enter current date and time (YYYY-MM-DD HH:MM): ")
    duration_h = int(input("Meeting duration (hours): "))
    duration_m = int(input("Meeting duration (minutes): "))

    start = datetime.datetime.strptime(now_str, "%Y-%m-%d %H:%M")
    end = start + datetime.timedelta(hours=duration_h, minutes=duration_m)

    print(f"Meeting will end at: {end.strftime('%Y-%m-%d %H:%M')}")

def timezone_converter():
    dt_str = input("Enter date and time (YYYY-MM-DD HH:MM): ")
    from_tz_str = input("Enter your current timezone (e.g., Asia/Tashkent): ")
    to_tz_str = input("Enter target timezone (e.g., Europe/London): ")

    dt_naive = datetime.datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
    from_tz = pytz.timezone(from_tz_str)
    to_tz = pytz.timezone(to_tz_str)

    dt_local = from_tz.localize(dt_naive)
    dt_converted = dt_local.astimezone(to_tz)

    print(f"Time in {to_tz_str}: {dt_converted.strftime('%Y-%m-%d %H:%M')}")

def countdown_timer():
    future_str = input("Enter future date and time (YYYY-MM-DD HH:MM:SS): ")
    future_time = datetime.datetime.strptime(future_str, "%Y-%m-%d %H:%M:%S")

    while True:
        now = datetime.datetime.now()
        if future_time <= now:
            print("Time is up!")
            break

        delta = future_time - now
        print(f"Time remaining: {delta}", end='\r')
        time.sleep(1)

def email_validator():
    email = input("Enter an email address: ")
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    if re.match(pattern, email):
        print("Valid email address.")
    else:
        print("Invalid email address.")

def phone_number_formatter():
    phone = input("Enter a 10-digit phone number: ")
    digits = re.sub(r'\D', '', phone)
    if len(digits) == 10:
        formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        print(f"Formatted: {formatted}")
    else:
        print("Invalid input. Please enter exactly 10 digits.")

def password_strength_checker():
    password = input("Enter a password: ")
    errors = []
    if len(password) < 8:
        errors.append("Minimum length is 8.")
    if not re.search(r'[A-Z]', password):
        errors.append("Must contain at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        errors.append("Must contain at least one lowercase letter.")
    if not re.search(r'\d', password):
        errors.append("Must contain at least one digit.")

    if errors:
        print("Weak password:")
        for err in errors:
            print("-", err)
    else:
        print("Strong password.")

def word_finder():
    sample_text = """This is a sample text. You can search for a specific word in this text. Let's find the word."""
    word = input("Enter the word to search for: ").lower()
    found = re.findall(rf'\b{re.escape(word)}\b', sample_text.lower())
    print(f"Occurrences of '{word}': {len(found)}")

def date_extractor():
    text = input("Enter text containing dates: ")
    dates = re.findall(r'\b\d{4}-\d{2}-\d{2}\b', text)
    print("Dates found:")
    for d in dates:
        print(d)

# Menu
functions = {
    '1': age_calculator,
    '2': days_until_next_birthday,
    '3': meeting_scheduler,
    '4': timezone_converter,
    '5': countdown_timer,
    '6': email_validator,
    '7': phone_number_formatter,
    '8': password_strength_checker,
    '9': word_finder,
    '10': date_extractor
}

def main():
    while True:
        print("\nHomework Menu:")
        for key, func in functions.items():
            print(f"{key}. {func.__name__.replace('_', ' ').title()}")
        print("0. Exit")

        choice = input("Choose a number (0-10): ").strip()
        if choice == '0':
            break
        elif choice in functions:
            print()
            functions[choice]()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
