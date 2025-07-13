import pytest
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import AUTH_URL, TEST_USER_CREDENTIALS, DEFAULT_TIMEOUT
def test_login_success(driver):
    # Open Website to Login
    driver.get(AUTH_URL)

    # Initialize the LoginPage object
    login_page = LoginPage(driver)

    # Execute the login process
    login_page.login(TEST_USER_CREDENTIALS["email"], TEST_USER_CREDENTIALS["password"])

    # Wait for the URL to change after a successful login
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(EC.url_changes(AUTH_URL))

    # Check if the URL has changed (which indicates a successful login)
    assert driver.current_url != AUTH_URL
