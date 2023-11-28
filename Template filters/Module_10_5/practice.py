from datetime import datetime

# Your time string in a specific format
time_string = "2023-11-28 12:30:00"

# Specify the format of your time string
format_string = "%Y-%m-%d %H:%M:%S"

# Use strptime to convert the string to a datetime object
datetime_object = datetime.strptime(time_string, format_string)

print(datetime_object)
