import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from helpers.cart_utils import clear_cart, add_items_to_cart, open_shop_and_handle_dob
from config import AUTH_URL, STORE_URL, CHECKOUT_URL, TEST_PRODUCTS, TEST_USER_CREDENTIALS

# 1️⃣ Shipping Test Cases (1., 2., 3.)
@pytest.mark.parametrize("product_name, quantity, expected_shipping", [
    (TEST_PRODUCTS["shipping_product"], 9, "5€"),
    (TEST_PRODUCTS["shipping_product"], 10, "0€"),
    (TEST_PRODUCTS["shipping_product"], 11, "0€")
])
def test_shipping_threshold(driver, product_name, quantity, expected_shipping):
    driver.get(AUTH_URL)

    login_page = LoginPage(driver)
    login_page.login(TEST_USER_CREDENTIALS["email"], TEST_USER_CREDENTIALS["password"])

    open_shop_and_handle_dob(driver)
    clear_cart(driver)
    driver.get(STORE_URL)
    add_items_to_cart(driver, product_name, quantity)

    driver.get(CHECKOUT_URL)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'shipment-container')]"))
    )

    checkout_page = CheckoutPage(driver)
    actual_shipping = checkout_page.get_shipping_cost()

    assert actual_shipping == expected_shipping

# 2️⃣ 4th Test Case – Smanjivanje količine ispod granice za besplatnu dostavu
def test_shipping_becomes_paid_after_removing_item(driver):
    driver.get(AUTH_URL)

    LoginPage(driver).login(TEST_USER_CREDENTIALS["email"], TEST_USER_CREDENTIALS["password"])
    open_shop_and_handle_dob(driver)
    clear_cart(driver)
    driver.get(STORE_URL)

    # Dodaj 21 proizvod
    add_items_to_cart(driver, product_name=TEST_PRODUCTS["cheap_product"], quantity=21)

    driver.get(CHECKOUT_URL)

    # Sačekaj da se učita shipping info prije nego klikneš minus
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'shipment-container')]"))
    )

    checkout_page = CheckoutPage(driver)

    checkout_page.click_minus_button_multiple_times(2)

    # Pričekaj da se shipping info promijeni
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.XPATH, "//div[contains(@class, 'shipment-container')]"), "€"
        )
    )

    shipping_text = checkout_page.get_updated_shipping_after_refresh()
    print(f"[INFO] Shipping cost after decreasing quantity: '{shipping_text}'")

    assert "0" not in shipping_text and "free" not in shipping_text.lower(), \
        "❌ Shipping is still free after reducing the total below the threshold."
