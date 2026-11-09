from dataclasses import dataclass
from datetime import datetime, timedelta

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




@dataclass(frozen=True)
class Booking:
    client: str
    service: Service
    start: datetime

    def end_time(self) -> datetime:
        return self.start + timedelta(minutes=self.service.duration)