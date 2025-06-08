import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage

@pytest.fixture(scope="function")
def purchase_product_once(driver):
    driver.get("https://grocerymate.masterschool.com/auth")

    # Login
    LoginPage(driver).login("lucicmiroslav1989@gmail.com", "Mico5566")

    # Shop
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/store']"))
    ).click()

    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='DD-MM-YYYY']"))
        ).send_keys("01-01-2000")
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
        street="Test ulica 1",
        city="Testgrad",
        zip_code="75000",
        card_number="4111111111111111",
        name_on_card="Miroslav Lucic",
        expiry="10/2028",
        cvc="123"
    )
    checkout.click_buy_now()

    print("✅ The product has been purchased only ONCE for all tests.")

    time.sleep(3)

    # ⬇️ IMPORTANT! Manually return to the Store as the app doesn't redirect automatically
    driver.get("https://grocerymate.masterschool.com/store")

