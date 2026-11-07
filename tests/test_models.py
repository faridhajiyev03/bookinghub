import pytest
from dataclasses import FrozenInstanceError
from booking.models import Service

def test_service_is_frozen():
    service = Service("Haircut", 30.0, 60)
    with pytest.raises(FrozenInstanceError):
        service.price = 5.0

def test_service_keeps_fields():
    name, price, duration = "Haircut", 30.0, 60

    service = Service(name, price, duration)

    assert service.name == "Haircut"
    assert service.price == 30.0
    assert service.duration == 60

@pytest.mark.parametrize(
    "name, price, duration, message",
    [
        ("", 30.0, 60, "Name cannot be empty"),
        ("   ", 30.0, 60, "Name cannot be empty"),
        ("Haircut", -1.0, 60, "Price cannot be negative"),
        ("Haircut", 30.0, 0, "Duration must be positive"),
        ("Haircut", 30.0, -5, "Duration must be positive"),
    ],
)
def test_service_rejects_invalid_data(name, price, duration, message):
    with pytest.raises(ValueError, match=message):
        Service(name, price, duration)