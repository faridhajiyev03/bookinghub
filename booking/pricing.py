from .models import Service

def apply_discount(price: float, discount: float) -> float:
    if not (0 <= discount <= 100):
        raise ValueError("Discount must be between 0 and 100")
    return price - (price * discount) / 100

def service_price_with_discount(service:Service, percent:float)->float:
    return apply_discount(service.price, percent)

if __name__ == "__main__":
    print(service_price_with_discount(Service("Haircut", 30.0, 60), 10))