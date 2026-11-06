from dataclasses import dataclass, field
from datetime import datetime, timedelta

def overlaps(start1: datetime, end1: datetime,
             start2: datetime, end2: datetime) -> bool:
    return not (end1 <= start2 or end2 <= start1)



@dataclass(frozen=True)
class Service:
    name: str
    price: float
    duration: int

    def __post_init__(self):
        if not self.name.strip():
            raise ValueError("Name cannot be empty")
        if self.price < 0:
            raise ValueError("Price cannot be negative")
        if self.duration <= 0:
            raise ValueError("Duration must be positive")


@dataclass()
class Booking:
    client: str
    service: Service
    start: datetime

    def end_time(self)->datetime:
        return self.start + timedelta(minutes=self.service.duration)

    def __str__(self)->str:
        return f"{self.client}: {self.service.name}, {self.start.strftime('%H:%M')}-{self.end_time().strftime('%H:%M')}"



@dataclass()
class Schedule:
    bookings: list[Booking] = field(default_factory=list)

    def add(self, booking: Booking) -> None:
        for existing in self.bookings:
            if overlaps(booking.start, booking.end_time(), existing.start, existing.end_time()):
                raise ValueError("Time slot is already taken")
        self.bookings.append(booking)


    def total_price(self) -> float:
          return sum(booking.service.price for booking in self.bookings)






schedule = Schedule()
haircut = Service("Haircut", 30.0, 60)
massage = Service("Massage", 50.0, 90)

attempts = [
    Booking("Anna", haircut, datetime(2026, 11, 10, 10, 0)),
    Booking("Rauf", massage, datetime(2026, 11, 10, 10, 30)),
    Booking("Leyla", massage, datetime(2026, 11, 10, 11, 0)),
]

for booking in attempts:
    try:
        schedule.add(booking)
        print(f"Added: {booking}")
    except ValueError as error:
        print(f"Error: {error}")

print(f"Total: {schedule.total_price()}")
print(len(schedule.bookings))