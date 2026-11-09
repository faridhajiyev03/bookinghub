from .models import Service

def apply_discount(price:float, discount:float)->float:
    return price - (price * discount) / 100

def service_price_with_discount(service:Service, percent:float)->float:
    return apply_discount(service.price, percent)

if __name__ == "__main__":
    print(service_price_with_discount(Service("Haircut", 30.0, 60), 10))