import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from config import AUTH_URL, STORE_URL, TEST_USER_CREDENTIALS, SHORT_TIMEOUT, DEFAULT_TIMEOUT, TEST_DOB,TEST_CHECKOUT_DATA


@pytest.fixture(scope="function")
def purchase_product_once(driver):
    driver.get(AUTH_URL)

    # Login
    LoginPage(driver).login(TEST_USER_CREDENTIALS)

    # Shop
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/store']"))
    ).click()

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='DD-MM-YYYY']"))
        ).send_keys(TEST_DOB)
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Confirm']"))
        ).click()
    except:
        print("Datum rođenja nije tražen.")

    # add in cart
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//img[@alt='Gala Apples']/ancestor::div[@class='card']//button[contains(text(), 'Add to Cart')]"))
    ).click()

    # Cart
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//div[@class='headerIcon'])[3]"))
    ).click()

    # Checkout
    checkout = CheckoutPage(driver)
    checkout.enter_checkout_details(
        street=TEST_CHECKOUT_DATA["street"],
        city=TEST_CHECKOUT_DATA["city"],
        zip_code=TEST_CHECKOUT_DATA["postcode"],
        card_number=TEST_CHECKOUT_DATA["card_number"],
        name_on_card=TEST_CHECKOUT_DATA["card_name"],
        expiry=TEST_CHECKOUT_DATA["card_expiry"],
        cvc=TEST_CHECKOUT_DATA["card_cvc"]
    )
    checkout.click_buy_now()

    print("✅ The product has been purchased only ONCE for all tests.")

    time.sleep(3)

    # ⬇️ IMPORTANT! Manually return to the Store as the app doesn't redirect automatically
    driver.get(STORE_URL)

