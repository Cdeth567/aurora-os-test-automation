import pytest

@pytest.fixture
def app_name():
    return "Aurora Demo"

def test_app_name(app_name):
    assert app_name == "Aurora Demo"