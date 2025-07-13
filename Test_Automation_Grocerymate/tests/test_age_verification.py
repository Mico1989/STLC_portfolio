from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
import pytest
import time
from config import AUTH_URL, TEST_USER_CREDENTIALS, INVALID_DOB
from pages.shop_page import ShopPage
from datetime import datetime, timedelta


# Age Verification Test Cases (1st, 2end, 3r)
@pytest.mark.parametrize("birth_date, expected", [
    ((datetime.now() - timedelta(days=18*365)).strftime("%d-%m-%Y"), "store"),      # tačno 18
    ((datetime.now() - timedelta(days=17*365)).strftime("%d-%m-%Y"), "underage"),   # mlađi
    ((datetime.now() - timedelta(days=19*365)).strftime("%d-%m-%Y"), "store"),      # stariji
])
def test_age_verification(driver, birth_date, expected):
    driver.get(AUTH_URL)

    login_page = LoginPage(driver)
    login_page.login(TEST_USER_CREDENTIALS["email"], TEST_USER_CREDENTIALS["password"])

    shop_page = ShopPage(driver)

    shop_page.process_age_verification(birth_date)
    time.sleep(2)

    if expected == "store":
        assert "store" in driver.current_url
    elif expected == "underage":
        assert "underage" in shop_page.get_error_message()

# Age Verification 4th Test Case
def test_age_verification_empty_date(driver):
    driver.get(AUTH_URL)

    login_page = LoginPage(driver)
    login_page.login(TEST_USER_CREDENTIALS["email"], TEST_USER_CREDENTIALS["password"])


    shop_page = ShopPage(driver)
    shop_page.submit_empty_dob()

    assert "underage" in shop_page.get_error_message()

# Age Verification 5th Test Case
def test_age_verification_invalid_format(driver):
    driver.get(AUTH_URL)

    login_page = LoginPage(driver)
    login_page.login(TEST_USER_CREDENTIALS["email"], TEST_USER_CREDENTIALS["password"])

    shop_page = ShopPage(driver)
    shop_page.open_store_page()
    shop_page.enter_date_of_birth(INVALID_DOB)
    shop_page.submit_age_verification()

    assert "underage" in shop_page.get_error_message()








