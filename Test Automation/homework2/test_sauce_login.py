import pytest
from selenium.webdriver.common.by import By
import time

@pytest.mark.parametrize("username", [
    "standard_user",
    "locked_out_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user"
])
def test_login_and_verify_product(driver, username):
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    # Login
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)  # da se stranica učita

    if username == "locked_out_user":
        error_msg = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
        assert "locked out" in error_msg
    else:
        # Provjera da smo logovani
        title = driver.find_element(By.CLASS_NAME, "title").text
        assert title == "Products"

        # Provjera da proizvod postoji
        product = driver.find_element(By.XPATH, "//div[text()='Sauce Labs Backpack']")
        assert product.is_displayed()
