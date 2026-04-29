import json
import pytest

@pytest.fixture
def cart_data():
    with open('data/cart_data.json') as f:
        return json.load(f)