from booking.pricing import apply_discount
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
