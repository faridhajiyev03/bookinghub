def load_bookings(filename: str) -> list:
    lines = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                lines.append(line.strip())
    except FileNotFoundError:
        return []
    return lines

print(load_bookings("bookings.txt"))
print(load_bookings("missing.txt"))