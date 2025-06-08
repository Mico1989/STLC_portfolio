from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
import pytest
import time

from pages.shop_page import ShopPage

# Age Verification Test Cases (1st, 2end, 3r)
@pytest.mark.parametrize("birth_date, expected", [
    ("16-05-2006", "store"),        # tačno 18 godina
    ("01-01-2008", "underage"),     # mlađi od 18
    ("16-05-2005", "store")         # stariji od 18
])
def test_age_verification(driver, birth_date, expected):
    driver.get("https://grocerymate.masterschool.com/auth")

    login_page = LoginPage(driver)
    login_page.login("johndoe@example1.com", "M@rketM@te25")

    shop_page = ShopPage(driver)

    shop_page.process_age_verification(birth_date)
    time.sleep(2)

    if expected == "store":
        assert "store" in driver.current_url
    elif expected == "underage":
        assert "underage" in shop_page.get_error_message()

# Age Verification 4th Test Case
def test_age_verification_empty_date(driver):
    driver.get("https://grocerymate.masterschool.com/auth")

    login_page = LoginPage(driver)
    login_page.login("johndoe@example1.com", "M@rketM@te25")

    shop_page = ShopPage(driver)
    shop_page.submit_empty_dob()

    assert "underage" in shop_page.get_error_message()

# Age Verification 5th Test Case
def test_age_verification_invalid_format(driver):
    driver.get("https://grocerymate.masterschool.com/auth")

    login_page = LoginPage(driver)
    login_page.login("johndoe@example1.com", "M@rketM@te25")

    shop_page = ShopPage(driver)
    shop_page.open_store_page()
    shop_page.enter_date_of_birth("32-12-2006")
    shop_page.submit_age_verification()

    assert "underage" in shop_page.get_error_message()








