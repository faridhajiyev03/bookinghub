import pytest
from datetime import datetime

from booking.schedule import overlaps


@pytest.mark.parametrize(
    "s1, e1, s2, e2, expected",
    [
        (10, 12, 11, 13, True),  # частичное пересечение
        (10, 14, 11, 12, True),  # один внутри другого
        (10, 11, 11, 12, False),  # касаются границами
        (10, 11, 12, 13, False),  # далеко друг от друга
    ],
)
def test_overlaps(s1, e1, s2, e2, expected):
    d = lambda hour: datetime(2026, 11, 7, hour)
    assert overlaps(d(s1), d(e1), d(s2), d(e2)) == expected