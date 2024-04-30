from datetime import datetime
current_datetime = datetime.now()
print("Current Date and Time:", current_datetime)
formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted Date:", formatted_date)
date_string = "2023-12-02"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
print("Parsed Date:", parsed_date)
from datetime import timedelta
next_week = current_datetime + timedelta(weeks=1)
print("Next Week:", next_week)