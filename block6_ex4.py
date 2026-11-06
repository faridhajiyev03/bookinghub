class Service:
    def __init__(self, name, price, duration):
        self.name = name
        self.price = price
        self.duration = duration

    def __str__(self)->str:
        return f"{self.name}: {self.price} AZN {self.duration} min"

    def __repr__(self)->str:
        return f"Service(name={self.name!r}, price={self.price!r}, duration={self.duration!r})"

haircut = Service("Haircut", 30.0, 60)
massage = Service("Massage", 50.0, 90)

print(haircut)
print(f"Chosen: {massage}")
print(repr(haircut))
print([haircut, massage])