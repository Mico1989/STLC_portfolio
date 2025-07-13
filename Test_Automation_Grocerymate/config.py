#URLS
BASE_URL = "https://grocerymate.masterschool.com"
AUTH_URL = f"{BASE_URL}/auth"
STORE_URL = f"{BASE_URL}/store"
CHECKOUT_URL = f"{BASE_URL}/checkout"
CART_URL = f"{BASE_URL}/cart"

# Timeouts
DEFAULT_TIMEOUT = 10
SHORT_TIMEOUT = 3
LONG_TIMEOUT = 20  # ako ti ikad zatreba

# Test checkout infos
TEST_CHECKOUT_DATA = {
    "street": "Test ulica 1",
    "city": "Testgrad",
    "postcode": "75000",
    "card_number": "4111111111111111",
    "card_name": "Miroslav Lucic",
    "card_expiry": "10/2028",
    "card_cvc": "123"
}

# Test login credentials
TEST_USER_CREDENTIALS = {
    "email": "lucicmiroslav1989@gmail.com",
    "password": "Mico5566"
}

# Test date of birth
TEST_DOB = "01-01-2000"

INVALID_DOB = "32-12-2006"

#items
TEST_PRODUCTS = {
    "rating_product": "Gala Apples",
    "shipping_product": "Gala Apples",
    "cheap_product": "Kale"

}

#
SHIPPING_COST_EXPECTED = {
    "below_20": "2.00 €",
    "equal_20": "0.00 €",
    "above_20": "0.00 €"
}


