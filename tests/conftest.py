import pytest
from booking.models import Service


@pytest.fixture
def haircut():
    return Service("Haircut", 30.0, 60)

@pytest.fixture
def massage():
    return Service("Massage", 50.0, 90)