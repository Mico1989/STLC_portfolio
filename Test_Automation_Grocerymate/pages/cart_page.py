from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import CHECKOUT_URL, SHORT_TIMEOUT
class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.shipping_info = (By.XPATH, "//div[contains(@class, 'shipping-cost')]")
        self.remove_icon = (By.XPATH, "//a[@class='remove-icon']")

    def clear_cart(self):
        self.driver.get(CHECKOUT_URL)
        try:
            while True:
                remove_btn = WebDriverWait(self.driver, 3).until(
                    EC.element_to_be_clickable(self.remove_icon)
                )
                remove_btn.click()
        except:
            print("Cart is empty or already cleared.")



    def get_shipping_text(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.shipping_info)
        ).text
