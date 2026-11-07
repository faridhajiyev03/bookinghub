class Service:
    def __init__ (self, name: str, price: float, duration: int):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if duration <= 0:
            raise ValueError("Duration must be positive")


        self.name = name
        self.price = price
        self.duration = duration

    def __str__(self)->str:
        return f"{self.name}: {self.price} AZN, {self.duration} min"

    def __repr__(self)->str:
        return f"Service(name={self.name!r}, price={self.price!r}, duration={self.duration!r})"


tests = [
    ("Haircut", 30.0, 60),
    ("", 30.0, 60),
    ("Massage", -5.0, 90),
    ("Facial", 40.0, 0),
]

for name, price, duration in tests:
    try:
        service = Service(name, price, duration)
        print(f"Created: {service}")
    except ValueError as error:
        print(f"Error: {error}")