
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from helpers.cart_utils import clear_cart, add_items_to_cart, open_shop_and_handle_dob

#  Shipping Cost Test Cases (1st, 2nd, 3rd)
@pytest.mark.parametrize("product_name, quantity, expected_shipping", [
    ("Gala Apples", 9, "5€"),
    ("Gala Apples", 10, "0€"),
    ("Gala Apples", 11, "0€")
])
def test_shipping_threshold(driver, product_name, quantity, expected_shipping):
    driver.get("https://grocerymate.masterschool.com/auth")

    login_page = LoginPage(driver)
    login_page.login("lucicmiroslav1989@gmail.com", "Mico5566")

    open_shop_and_handle_dob(driver)
    clear_cart(driver)
    driver.get("https://grocerymate.masterschool.com/store")
    add_items_to_cart(driver, product_name, quantity)

    driver.get("https://grocerymate.masterschool.com/checkout")
    driver.refresh()

    checkout_page = CheckoutPage(driver)
    actual_shipping = checkout_page.get_shipping_cost()
    assert actual_shipping == expected_shipping

# 4th Shipping Cost Test Case: Verify system behavior when a user removes items from the cart,
# causing the total to fall below the free shipping threshold.
def test_shipping_becomes_paid_after_removing_item(driver):
    driver.get("https://grocerymate.masterschool.com/auth")

    LoginPage(driver).login("lucicmiroslav1989@gmail.com", "Mico5566")

    open_shop_and_handle_dob(driver)

    clear_cart(driver)

    driver.get("https://grocerymate.masterschool.com/store")

    # Add 21 Items (Kale - 1€)
    add_items_to_cart(driver, product_name="Kale", quantity=21)
    time.sleep(2)

    driver.get("https://grocerymate.masterschool.com/checkout")
    checkout_page = CheckoutPage(driver)
    time.sleep(2)

    #Click the minus button twice to reduce the quantity to 19

    checkout_page.click_minus_button_multiple_times(2)
    time.sleep(2)

    # 7. Refresh + take shipping info
    shipping_text = checkout_page.get_updated_shipping_after_refresh()
    print(f"[INFO] Shipping cost after decreasing quantity: '{shipping_text}'")

    #  The shipping is expected to no longer be free
    assert "0" not in shipping_text and "free" not in shipping_text.lower(), \
        "❌ Shipping is still free after reducing the total below the threshold."



