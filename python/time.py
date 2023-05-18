from datetime import datetime

time_format = "%H:%M"

start_time = datetime.strptime("10:00", time_format)
end_time = datetime.strptime("13:34", time_format)

duration = end_time - start_time
hours = duration.total_seconds() / 3600
print(duration)
print(type(duration))
print(hours)