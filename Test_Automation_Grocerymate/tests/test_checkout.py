from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_successful_checkout(driver):
    driver.get("https://grocerymate.masterschool.com/auth")

    # Login
    login_page = LoginPage(driver)
    login_page.login("lucicmiroslav1989@gmail.com", "Mico5566")

    # Go to the Shop manually as the app doesn't redirect by itself
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='/store']"))
    ).click()

    time.sleep(4)

    # Enter date of birth if the modal appears
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='DD-MM-YYYY']"))
        ).send_keys("01-01-2000")

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Confirm']"))
        ).click()
    except:
        pass  # If the modal does not appear, proceed with the next steps

    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "modal-overlay"))
    )
    assert "store" in driver.current_url

    # Adding items to the cart
    driver.find_element(By.CLASS_NAME, "btn-cart").click()

    # Click on the Cart
    driver.get("https://grocerymate.masterschool.com/checkout")
    assert "checkout" in driver.current_url

    time.sleep(5)

    # Checkout Form
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_form(
        street="test1",
        city="test1",
        zip_code="75000",
        card_number="4111111111111111",
        name_on_card="Lucic Miroslav",
        expiry="10/2028",
        cvc="123"
    )

    time.sleep(3)
