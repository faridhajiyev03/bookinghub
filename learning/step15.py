from datetime import datetime

existing = [
    (datetime(2026, 11, 4, 10, 0), datetime(2026, 11, 4, 11, 0)),
    (datetime(2026, 11, 4, 13, 0), datetime(2026, 11, 4, 14, 0)),
]

def overlaps(start1: datetime, end1: datetime,
             start2: datetime, end2: datetime) -> bool:
    return not (end1 <= start2 or end2 <= start1)

def can_book(new_start: datetime, new_end: datetime, bookings: list) -> bool:
    if new_end <= new_start:
        raise ValueError("End must be after start")

    for start, end in bookings:
        if overlaps(new_start, new_end, start, end):
            return False
    return True




print(can_book(datetime(2026, 11, 4, 12, 0), datetime(2026, 11, 4, 11, 0), existing))

# try:
#     result = can_book(datetime(2026, 11, 4, 12, 0), datetime(2026, 11, 4, 12, 0), existing)
#     print(result)
# except ValueError as error:
#     print(f"Error: {error}")