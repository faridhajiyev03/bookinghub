with open("bookings.txt", "w", encoding="utf-8") as file:
    file.write("haircut\n")
    file.write("massage\n")
    file.write("manicure\n")

with open("bookings.txt", "r", encoding="utf-8") as file:
    content = file.read()
print(content)

with open("bookings.txt", "a", encoding="utf-8") as file:
    file.write("facial\n")

with open("bookings.txt", "r", encoding="utf-8") as file:
    content = file.read()
print(content)

