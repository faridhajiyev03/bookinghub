
while True:
    try:
        age = int(input("Enter your age "))
        print(f"Next year you will be: {age + 1}")
        break
    except ValueError:
        print("Please enter a number")

print("Program finished")







