from booking.pricing import apply_discount
from booking.pricing import service_price_with_discount
import pytest




@pytest.mark.parametrize(
    "price, percent, expected",
    [
        (30.0, 10, 27.0),
        (30.0, 0, 30.0),
        (30.0, 100, 0.0),
    ],
)
def test_apply_discount(price, percent, expected):
    assert apply_discount(price, percent) == expected




def test_haircut_with_discount(haircut):
    assert service_price_with_discount(haircut, 10) == 27.0

def test_massage_with_discount(massage):
    assert service_price_with_discount(massage, 20) == 40.0