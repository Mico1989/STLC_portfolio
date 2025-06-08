from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class ShopPage:
    STORE_XPATH = (By.XPATH, "//a[@href='/store']")
    DOB_XPATH = (By.XPATH, "//input[@placeholder='DD-MM-YYYY']")
    CONFIRM_BUTTON_XPATH = (By.XPATH, "//div[@class='modal-content']//button[text() = 'Confirm']")
    AGE_VERIFICATION_ERROR_XPATH = (By.XPATH, "//div[contains(text(),'underage')]")

    def __init__(self, driver):
        self.driver = driver

    def open_store_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.STORE_XPATH)
        ).click()

    def enter_date_of_birth(self, dob):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.DOB_XPATH)
        ).send_keys(dob)

    def submit_age_verification(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.CONFIRM_BUTTON_XPATH)
        ).click()

    def get_error_message(self):
        error_element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(self.AGE_VERIFICATION_ERROR_XPATH)
        )
        return error_element.text

    def process_age_verification(self, dob):
        self.open_store_page()
        self.enter_date_of_birth(dob)
        self.submit_age_verification()

    def submit_empty_dob(self):
        self.open_store_page()
        self.submit_age_verification()


