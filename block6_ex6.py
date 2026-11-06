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

    def __str__(self)->str:
        return f"{self.name}: {self.price} AZN, {self.duration} min"



a = Service("Haircut", 30.0, 60)
b = Service("Haircut", 30.0, 60)

print(a)
print(repr(a))
print(a == b)
print(a is b)

try:
    Service("", 30.0, 60)
except ValueError as error:
    print(f"Error: {error}")








