import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from config import AUTH_URL, TEST_USER_CREDENTIALS, TEST_CHECKOUT_DATA, TEST_DOB, DEFAULT_TIMEOUT, SHORT_TIMEOUT, STORE_URL


@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.delete_all_cookies()
    driver.quit()


@pytest.fixture(scope="function")
def purchase_product_once(driver):
    driver.get(AUTH_URL)

    LoginPage(driver).login(TEST_USER_CREDENTIALS["email"], TEST_USER_CREDENTIALS["password"])

    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/store']"))
    ).click()

    try:
        WebDriverWait(driver, SHORT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='DD-MM-YYYY']"))
        ).send_keys(TEST_DOB)
        WebDriverWait(driver, SHORT_TIMEOUT).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Confirm']"))
        ).click()
    except Exception:
        print("🟡 Date of birth was not requested.")

    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable((By.XPATH, "//img[@alt='Gala Apples']/ancestor::div[@class='card']//button[contains(text(), 'Add to Cart')]"))
    ).click()

    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable((By.XPATH, "(//div[@class='headerIcon'])[3]"))
    ).click()

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

    print("✅ The product was purchased ONCE for all tests.")
    time.sleep(3)
    driver.get(STORE_URL)
