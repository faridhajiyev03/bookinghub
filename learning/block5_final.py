import json

FILENAME = "bookinghub_data.json"



def save_hours(hours: list, filename: str) -> None:
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(hours, file)

def load_hours(filename: str) -> list:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def add_booking(hour: int, filename: str) -> None:
    booked = load_hours(filename)

    if hour < 9 or hour > 17:
        raise ValueError("Hour must be between 9 and 17")

    if hour in booked:
        raise ValueError("Hour already booked")

    booked.append(hour)
    save_hours(booked, filename)


try:
    add_booking(10, FILENAME)
    print("Booked: 10")
except ValueError as error:
    print(f"Error: {error}")

try:
    add_booking(20, FILENAME)
    print("Booked: 10")
except ValueError as error:
    print(f"Error: {error}")

try:
    add_booking(11, FILENAME)
    print("Booked: 10")
except ValueError as error:
    print(f"Error: {error}")





print(f"Final: {load_hours(FILENAME)}")