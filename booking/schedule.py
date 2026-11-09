from dataclasses import dataclass, field
from booking.models import Booking
from datetime import datetime



def overlaps(start1: datetime, end1: datetime, start2: datetime, end2: datetime) -> bool:
    return not (end1 <= start2 or end2 <= start1)

@dataclass
class Schedule:

    bookings: list[Booking] = field(default_factory=list)

    def add(self, booking: Booking)->None:
        for existing in self.bookings:
            if overlaps(booking.start, booking.end_time(), existing.start, existing.end_time()):
                raise ValueError("Time slot is already taken")
        self.bookings.append(booking)

