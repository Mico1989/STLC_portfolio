from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers.cart_utils import open_shop_and_handle_dob
from config import STORE_URL


class RatingPage:
    def __init__(self, driver):
        self.driver = driver

    def open_product_from_shop(self, product_name):
        self.driver.get(STORE_URL)
        open_shop_and_handle_dob(self.driver)

        #WebDriverWait(self.driver, 10).until(
         #   EC.element_to_be_clickable((By.XPATH, f"//h5[text()='{product_name}']"))
        #).click()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//img[@alt='{product_name}']"))
        ).click()

    def delete_existing_rating_if_exists(self):
        try:
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "(//div[@class='comment']//div[@class='menu-icon'])[1]"))
            ).click()
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='dropdown-menu']//button[text()='Delete']"))
            ).click()

            # 🔔 Handle the alert that appears
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            alert.accept()
            print("✅ Alert accepted – review deleted.")
        except:
            print("ℹ️ No review to delete or alert was not displayed.")
##
    def rate_product(self, stars):
        xpath = f"//div[@class='interactive-rating']//span[contains(@class, 'star')][{stars}]"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        ).click()

    def submit_review(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'new-review-btn-send')]"))
        ).click()

    def verify_rating_success_message(self):
        try:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((
                    By.XPATH,
                    "//p[contains(text(), 'You have already reviewed this product')]"
                ))
            )
            print("✅ Rating submitted – a message indicating the review was already submitted is displayed.")
        except:
            raise AssertionError("❌ No message indicating the rating was already submitted – something is wrong.")

    def verify_error_message(self, expected_text):
        try:
            xpath = f'//*[contains(text(), "{expected_text}")]'
            error_element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            assert expected_text in error_element.text
        except:
            raise AssertionError(f"❌ The expected error message was not found: '{expected_text}'")


