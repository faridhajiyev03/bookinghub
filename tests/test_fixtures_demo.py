import pytest

@pytest.fixture
def bag():
    return []

def test_first(bag):
    bag.append("apple")
    assert bag == ["apple"]

def test_second(bag):
    assert bag == []