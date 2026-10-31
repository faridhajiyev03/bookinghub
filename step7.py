booked_hours = []

running = True

while running:
    hour = int(input('Enter hour: '))
    if hour == 0:
        running = False
    elif hour < 9 or hour > 17:
        print('Invalid hour')
    elif hour in booked_hours:
        print('Already booked')
    else:
        booked_hours.append(hour)
        print(f'Booked: {hour:02d}:00')
print(booked_hours)

