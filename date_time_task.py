
from datetime import datetime

now = datetime.now()
print(f"Current Year: {now.year}")
print(f"Current Month: {now.month}")

date_string = input("Please enter a date in the format 'YYYY-MM-DD': ")
try:
    date_object = datetime.strptime(date_string, "%Y-%m-%d")
    print(f"Date Object: {date_object}")
except ValueError:
    print("Invalid date format. Please use 'YYYY-MM-DD'.")
