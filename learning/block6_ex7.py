
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass(frozen=True)
class Service:
    name: str
    price: float
    duration: int

@dataclass()
class Booking:
    client: str
    service: Service
    start: datetime

    def end_time(self)->datetime:
        return self.start + timedelta(minutes=self.service.duration)

    def __str__(self)->str:
        return f"{self.client}: {self.service.name}, {self.start.strftime('%H:%M')}-{self.end_time().strftime('%H:%M')}"

haircut = Service("Haircut", 30.0, 60)
massage = Service("Massage", 50.0, 90)

bookings = [
    Booking("Anna", haircut, datetime(2026, 11, 10, 10, 0)),
    Booking("Rauf", massage, datetime(2026, 11, 10, 12, 0)),
    Booking("Leyla", haircut, datetime(2026, 11, 10, 15, 30)),
]

for booking in bookings:
    print(booking)

total = 0.0
for booking in bookings:
    total += booking.service.price
print(f"Total: {total}")








