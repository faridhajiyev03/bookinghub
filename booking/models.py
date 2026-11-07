from dataclasses import dataclass

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