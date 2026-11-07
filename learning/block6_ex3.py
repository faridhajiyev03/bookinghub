class Service:
    def __init__(self, name, price, duration):
        self.name = name
        self.price = price
        self.duration = duration

    def apply_discount(self, percent: float) -> None:
        self.price = self.price - self.price * percent / 100  # меняет сам объект

    def price_with_discount(self, percent: float) -> float:
        return self.price - self.price * percent / 100  # объект не трогает

a = Service("Haircut", price=30.0, duration=60)
b = Service("Haircut", price=30.0, duration=60)
c = a

c.price = 40.0
b.duration = 45

print(a.price, b.price, c.price)
print(a.duration, b.duration, c.duration)
print(a is c, a is b)
print(a == b)