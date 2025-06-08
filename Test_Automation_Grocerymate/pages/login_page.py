from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # Lokatori za polja email i password
        self.email_input = (By.XPATH, "//input[@placeholder='Email address']")
        self.password_input = (By.XPATH, "//input[@placeholder='Password']")
        self.login_button = (By.CLASS_NAME, "submit-btn")

    def login(self, email, password):
        wait = WebDriverWait(self.driver, 10)

        # Wait and fill in the email field
        email_field = wait.until(EC.presence_of_element_located(self.email_input))
        email_field.clear()
        email_field.send_keys(email)

        # Wait and fill in the password field
        password_field = wait.until(EC.presence_of_element_located(self.password_input))
        password_field.clear()
        password_field.send_keys(password)

        # Wait and Click on the Login button
        login_btn = wait.until(EC.element_to_be_clickable(self.login_button))
        login_btn.click()

        # ✅ Added: wait until the "Shop" button becomes visible, indicating that login was successful
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/store']")))
