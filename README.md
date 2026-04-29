# **Project Name: Cart Validation**

Automated testing via pytest ensures totals and discount logic are applied correctly.

#### **data/cart_data.json**
It has data about the item (quantity, price, name) to be added to the cart.

#### **src/cart.py**
It is the source file which has functions to add items to the cart, get total of the cart and to apply discount.

#### **tests/conftest.py**
It has the fixture to read the json file and get the item details.

#### **tests/test_cart.py**
It tests all the features of the cart.

#### **pytest.ini**
It is the config file which contains the Command Line arguments 
to run the pytest.
