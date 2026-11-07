class Service:
    def __init__(self, name, price, duration):
        self.name = name
        self.price = price
        self.duration = duration

haircut = Service("Haircut", price=30.0, duration=60)
massage = Service("Massage", price=50.0, duration=90)

print(f"{haircut.name}: {haircut.price} AZN, {haircut.duration} min")
print(f"{massage.name}: {massage.price} AZN, {massage.duration} min")