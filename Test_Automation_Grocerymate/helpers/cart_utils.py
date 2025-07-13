import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.shop_page import ShopPage
from config import AUTH_URL, STORE_URL, CHECKOUT_URL, TEST_DOB

def open_shop_and_handle_dob(driver):
    shop_page = ShopPage(driver)
    shop_page.open_store_page()

    try:
        shop_page.enter_date_of_birth("10-10-1990")
        shop_page.submit_age_verification()
        time.sleep(3)  # Poželjno da sačekamo redirekciju
        driver.get(STORE_URL)  # Ručno vratimo shop
        time.sleep(3)
    except:
        print("ℹ️ The Date of Birth modal did not appear.")


def add_items_to_cart(driver, product_name, quantity):
    for _ in range(quantity):
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,
                f"//img[@alt='{product_name}']/ancestor::div[contains(@class, 'product-card')]//button[contains(., 'Add to Cart')]"
            ))
        ).click()
        time.sleep(0.5)



def clear_cart(driver):
    driver.get(CHECKOUT_URL)
    try:
        while True:
            remove_btn = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@class='remove-icon']"))
            )
            remove_btn.click()
            time.sleep(1)
    except:
        print("ℹ️ The cart is empty or there are no items left to remove.")


from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage

def buy_product(driver, product_name):
    driver.get(AUTH_URL)

    # Login
    login = LoginPage(driver)
    login.login("lucicmiroslav1989@gmail.com", "Mico5566")

    # Open the Shop and enter date of birth (if required)
    open_shop_and_handle_dob(driver)

    # Add Item in Cart
    add_items_to_cart(driver, product_name, quantity=1)

    # Go to Checkout
    driver.get(CHECKOUT_URL)
    driver.refresh()

    # Fill in the required information and click "Buy now"
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
    checkout.click_buy_now()    ###  MOZDA IZBRISATI OVU LINIJU
    print("🛍️ Purchase completed.")


def ensure_product_purchased(driver, product_name):
    # Navigate to the Shop and verify if the "Rate this product" button is displayed
    driver.get(STORE_URL)
    open_shop_and_handle_dob(driver)

    try:
        WebDriverWait(driver, 7).until(
            EC.presence_of_element_located((By.XPATH, f"//img[@alt='{product_name}']"))
        ).click()

        # Ako postoji opcija za ocjenu, proizvod je kupljen
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'interactive-rating')]"))
        )
        print("✅ This product was already purchased – no additional purchase is required.")
    except:
        print("ℹ️ The product has not been purchased – starting the purchase process.")
        buy_product(driver, product_name)



def go_to_product_detail(driver, product_name):
# Navigates to the Store page, handles AGE modal if present, and opens the product detail page for the given product name.

    driver.get(STORE_URL)
    open_shop_and_handle_dob(driver)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//img[@alt='{product_name}']"))
    ).click()







