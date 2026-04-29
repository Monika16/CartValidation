import pytest
from src.cart import Cart

def test_add_items():
    cart = Cart()
    cart.add_item('laptop', 5000, 1)
    assert len(cart.items) == 1

def test_total_price():
    cart = Cart()
    cart.add_item('phone', 500, 2)
    assert  cart.get_total() == 1000

def test_discount():
    cart = Cart()
    cart.add_item('laptop', 1000, 1)
    discounted = cart.apply_discount(10)
    assert discounted == 900

def test_invalid_price():
    cart = Cart()
    with pytest.raises(ValueError):
        cart.add_item('case', -500, 2)

def test_no_quantity():
    cart = Cart()
    with pytest.raises(ValueError):
        cart.add_item('laptop', 500, 0)

def test_cart_totals(cart_data):
    for data in cart_data:
        cart = Cart()
        cart.add_item(data['name'], data['price'], data['quantity'])
        assert cart.get_total() == data['expected_result']




