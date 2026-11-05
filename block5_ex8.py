import json



def save_hours(hours: list, filename: str) -> None:
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(hours, file)

def load_hours(filename: str) -> list:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []




print(load_hours("booked.json"))
save_hours([10, 13, 15], "booked.json")
print(load_hours("booked.json"))