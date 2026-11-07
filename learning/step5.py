waiting_for_valid_hour = True


while waiting_for_valid_hour:
    hour = int(input("Enter the time: "))
    if hour < 9 or hour > 17:
        print("Invalid hour, try again")


    else:
        print(f'Slot booked: {hour:02d}:00')
        waiting_for_valid_hour = False


