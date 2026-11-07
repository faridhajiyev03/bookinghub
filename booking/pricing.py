from .models import Service

def apply_discount(price, discount):
    return price - (price * discount) / 100

def service_price_with_discount(service, percent):
    return apply_discount(service.price, percent)

if __name__ == "__main__":
    print(service_price_with_discount(Service("Haircut", 30.0, 60), 10))