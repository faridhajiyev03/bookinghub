def validate_hour(hour: int) -> int:
    if hour < 9 or hour > 17:
        raise ValueError("Hour must be between 9 and 17")
    return hour

try:
    hour = int(input("Enter hour: "))
    validate_hour(hour)
    print(f"Valid hour: {hour}")
except ValueError as error:
    print(f"Error: {error}")

