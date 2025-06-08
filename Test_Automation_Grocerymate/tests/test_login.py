import pytest
from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_success(driver):
    # Open Website to Login
    driver.get("https://grocerymate.masterschool.com/auth")

    # Initialize the LoginPage object
    login_page = LoginPage(driver)

    # Execute the login process
    login_page.login("lucicmiroslav1989@gmail.com", "Mico5566")

    # Wait for the URL to change after a successful login
    WebDriverWait(driver, 10).until(EC.url_changes("https://grocerymate.masterschool.com/auth"))

    # Check if the URL has changed (which indicates a successful login)
    assert driver.current_url != "https://grocerymate.masterschool.com/auth"
