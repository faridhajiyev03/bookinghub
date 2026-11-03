

from datetime import datetime

def overlaps(start1: datetime, end1: datetime,
             start2: datetime, end2: datetime) -> bool:
    return not (end1 < start2 or end2 <= start1)


a_start = datetime(2026, 11, 4, 10, 0)
a_end = datetime(2026, 11, 4, 11, 0)

print(overlaps(a_start, a_end, datetime(2026, 11, 4, 10, 30), datetime(2026, 11, 4, 11, 30)))  # case 1
print(overlaps(a_start, a_end, datetime(2026, 11, 4, 11, 0), datetime(2026, 11, 4, 12, 0)))    # case 2
print(overlaps(a_start, a_end, datetime(2026, 11, 4, 8, 0), datetime(2026, 11, 4, 9, 0)))      # case 3