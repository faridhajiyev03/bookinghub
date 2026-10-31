booked_hours = [10, 13, 15]

for hour in range(9, 18):
    if hour not in booked_hours:
        print(f'{hour:02d}:00 - free')
    elif hour in booked_hours:
        print(f'{hour:02d}:00 - booked')