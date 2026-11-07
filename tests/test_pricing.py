from booking.pricing import apply_discount

def test_apply_discount_ten_percent():
    assert apply_discount(30.0, 10) == 27.0

def test_apply_discount_zero_percent():
    assert apply_discount(30.0, 0) == 30.0

def test_apply_discount_hundred_percent():
    assert apply_discount(30.0, 100) == 10.0