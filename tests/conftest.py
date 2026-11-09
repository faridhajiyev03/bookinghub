import pytest
from booking.models import Service
from booking.schedule import Schedule


@pytest.fixture
def schedule():
    return Schedule()


@pytest.fixture
def haircut():
    return Service("Haircut", 30.0, 60)

@pytest.fixture
def massage():
    return Service("Massage", 50.0, 90)

