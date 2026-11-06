class Service:
    def __init__(self, name, price, duration):
        self.name = name
        self.price = price
        self.duration = duration

    def describe(self)->str:
        return f"{self.name}: {self.price} AZN, {self.duration} min"

    def price_with_discount(self, percent: float) -> float:
        return self.price - (self.price * percent) / 100

haircut = Service("Haircut", price=30.0, duration=60)
massage = Service("Massage", price=50.0, duration=90)

print(haircut.describe())
print(massage.describe())
print(haircut.price_with_discount(10))
print(massage.price_with_discount(20))