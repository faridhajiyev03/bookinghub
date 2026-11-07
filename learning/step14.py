def read_hour()->int:

    while True:
        try:
            hour = int(input("Enter hour: "))

            if hour < 9 or hour > 17:
                print("Hour must be between 9 and 17")

            else:
                return hour
        except ValueError:
            print("Please enter a number")

print(read_hour())




