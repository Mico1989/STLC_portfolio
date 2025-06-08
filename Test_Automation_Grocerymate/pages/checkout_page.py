from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

        # Lokatori
        self.street_address = (By.XPATH, "//input[@placeholder='Street Address']")
        self.city = (By.XPATH, "//input[@placeholder='City']")
        self.postal_code = (By.XPATH, "//input[@placeholder='Postal Code']")
        self.card_number = (By.XPATH, "//input[@placeholder='Card number']")
        self.card_name = (By.XPATH, "//input[@placeholder='Name on card']")
        self.card_expiry = (By.XPATH, "//input[@placeholder='Expiration']")
        self.card_cvc = (By.XPATH, "//input[@placeholder='Cvv']")
        self.buy_now_button = (By.XPATH, "//button[text()='Buy now']")

    def enter_checkout_details(self, street, city, zip_code, card_number, name_on_card, expiry, cvc, wait_time=10):
        wait = WebDriverWait(self.driver, wait_time)

        wait.until(EC.presence_of_element_located(self.street_address)).send_keys(street)
        wait.until(EC.presence_of_element_located(self.city)).send_keys(city)
        wait.until(EC.presence_of_element_located(self.postal_code)).send_keys(zip_code)

        wait.until(EC.presence_of_element_located(self.card_number)).send_keys(card_number)
        wait.until(EC.presence_of_element_located(self.card_name)).send_keys(name_on_card)
        wait.until(EC.presence_of_element_located(self.card_expiry)).send_keys(expiry)
        wait.until(EC.presence_of_element_located(self.card_cvc)).send_keys(cvc)

    def click_buy_now(self, wait_time=10):
        wait = WebDriverWait(self.driver, wait_time)
        wait.until(EC.element_to_be_clickable(self.buy_now_button)).click()

    def complete_checkout_with_test_data(self):
        self.enter_checkout_details(
            street="Test ulica 1",
            city="Testgrad",
            zip_code="75000",
            card_number="4111111111111111",
            name_on_card="Miroslav Lucic",
            expiry="10/2028",
            cvc="123"
        )
        self.click_buy_now()

    def get_shipping_cost(self, wait_time=10):
        wait = WebDriverWait(self.driver, wait_time)
        shipping_element = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='shipment-container']/h5[2]"))
        )
        return shipping_element.text.strip()

    def click_minus_button_multiple_times(self, times):
        for _ in range(times):
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='minus']"))
            ).click()
            time.sleep(1)

    def get_updated_shipping_after_refresh(self):
        self.driver.refresh()
        shipping_xpath = "//h5[text()='Shipment:']/following-sibling::h5"
        shipping_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, shipping_xpath))
        )
        return shipping_element.text.strip()


