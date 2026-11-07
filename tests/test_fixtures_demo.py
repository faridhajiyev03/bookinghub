import pytest

@pytest.fixture
def bag():
    return []

def test_first(bag):
    print(id(bag))
    bag.append("apple")
    assert bag == ["apple"]

def test_second(bag):
    print(id(bag))
    assert bag == []

def test_tmp_path_roundtrip(tmp_path):
    file = tmp_path / "data.txt"
    file.write_text("Haircut")
    assert file.read_text() == "Haircut"

@pytest.fixture
def resource():
    print("setup")
    yield "data"
    print("teardown")


def test_resource(resource):
    print("in test")
    assert resource == "data"