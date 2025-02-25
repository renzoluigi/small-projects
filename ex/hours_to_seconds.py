def hours_to_seconds(time):
    hours = int(time[:2])
    minutes = int(time[3:5])
    seconds = int(time[6:])
    return hours * 3600 + minutes * 60 + seconds
print(hours_to_seconds('10:09:24'))