from booking.models import Service
from booking.pricing import service_price_with_discount

print(service_price_with_discount(Service("Haircut", 30.0, 60), 10))