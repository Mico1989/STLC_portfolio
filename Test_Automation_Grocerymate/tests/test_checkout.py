from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config import AUTH_URL, TEST_USER_CREDENTIALS, TEST_CHECKOUT_DATA, SHORT_TIMEOUT, DEFAULT_TIMEOUT, TEST_DOB, CHECKOUT_URL

def test_successful_checkout(driver):
    driver.get(AUTH_URL)

    # Login
    login_page = LoginPage(driver)
    login_page.login(TEST_USER_CREDENTIALS["email"], TEST_USER_CREDENTIALS["password"])

    # Go to the Shop manually as the app doesn't redirect by itself
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/store']"))
    ).click()

    time.sleep(4)

    # Enter date of birth if the modal appears
    try:
        WebDriverWait(driver, SHORT_TIMEOUT).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='DD-MM-YYYY']"))
        ).send_keys(TEST_DOB)

        WebDriverWait(driver, SHORT_TIMEOUT).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Confirm']"))
        ).click()
    except:
        pass  # If the modal does not appear, proceed with the next steps

    WebDriverWait(driver, DEFAULT_TIMEOUT).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "modal-overlay"))
    )
    assert "store" in driver.current_url

    # Adding items to the cart
    driver.find_element(By.CLASS_NAME, "btn-cart").click()

    # Click on the Cart
    driver.get(CHECKOUT_URL)
    assert "checkout" in driver.current_url

    time.sleep(5)

    # Checkout Form
    checkout_page = CheckoutPage(driver)
    checkout_page.enter_checkout_details(
        street=TEST_CHECKOUT_DATA["street"],
        city=TEST_CHECKOUT_DATA["city"],
        zip_code=TEST_CHECKOUT_DATA["postcode"],
        card_number=TEST_CHECKOUT_DATA["card_number"],
        name_on_card=TEST_CHECKOUT_DATA["card_name"],
        expiry=TEST_CHECKOUT_DATA["card_expiry"],
        cvc=TEST_CHECKOUT_DATA["card_cvc"]
    )

    time.sleep(3)
