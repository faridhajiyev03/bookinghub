bookings = [("Anna", 10), ("Bob", 13), ("Anna", 15), ("Eva", 11), ("Bob", 16)]


unique_clients = set()
for booking in bookings:
    name, hour = booking
    unique_clients.add(name)
    print(f"{name}: {hour:02d}:00")

print(f"Unique clients: {len(unique_clients)}")