from datetime import datetime


def overlaps(start1: datetime, end1: datetime, start2: datetime, end2: datetime) -> bool:
    return not (end1 <= start2 or end2 <= start1)
