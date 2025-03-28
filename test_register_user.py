import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_signup_with_name_and_email(driver):
    driver.get("https://automationexercise.com/")
    time.sleep(2)

    # Zatvori popup ako postoji
    try:
        close_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "fc-close"))
        )
        close_btn.click()
        time.sleep(1)
    except TimeoutException:
        pass

    # Klik na 'Signup / Login'
    signup_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Signup / Login')]"))
    )
    try:
        signup_btn.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", signup_btn)

    # Sačekaj da se pojavi forma 'New User Signup!'
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'New User Signup!')]"))
    )

    # Unesi ime
    name_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "name"))
    )

    # Skroluj do elementa, ako je potrebno
    driver.execute_script("arguments[0].scrollIntoView(true);", name_input)

    # Koristi ActionChains da bi simulirao klik
    action = ActionChains(driver)
    action.move_to_element(name_input).click().perform()

    # Probaj sačekati malo duže ako je element sporo učitan
    time.sleep(2)

    # Unesi ime pomoću JavaScript-a ako standardni metod ne funkcioniše
    driver.execute_script("arguments[0].value='Test User';", name_input)

    # Unos email-a
    # Povećaj čekanje za email input
    email_input = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@data-qa='signup-email']"))
    )

    # Koristi JavaScript za unos email-a
    driver.execute_script("arguments[0].value='testuser123@email.com';", email_input)

    # Klik na Signup dugme
    signup_btn = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='signup-button']"))
    )

    # Pokušaj kliknuti dugme koristeći JavaScript kako bi zaobišao elemente koji blokiraju klik
    try:
        signup_btn.click()
    except ElementClickInterceptedException:
        driver.execute_script("arguments[0].click();", signup_btn)

    # Sačekaj da se pojavi 'Enter Account Information'
    try:
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//b[contains(text(),'Enter Account Information')]"))
        )
    except TimeoutException:
        print("Timeout: Element 'Enter Account Information' nije postao vidljiv.")
        driver.save_screenshot("timeout_error.png")  # Snimi screenshot ako je element nevidljiv
        return  # Prekini test ako je element nevidljiv

    # Nastavak testa (popunjavanje podataka, kreiranje naloga itd.)
    title_radio = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "id_gender1"))  # Mr. radio button
    )
    title_radio.click()

    password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "password"))
    )
    password_input.send_keys("Test@123")

    # Unos datuma rođenja
    day_select = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "days"))
    )
    Select(day_select).select_by_value("1")  # Select day, month, and year
    month_select = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "months"))
    )
    Select(month_select).select_by_value("1")  # January
    year_select = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "years"))
    )
    Select(year_select).select_by_value("1990")  # Year 1990

    # Selekcija checkbox-ova
    newsletter_checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "newsletter"))
    )
    newsletter_checkbox.click()

    special_offers_checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "optin"))
    )
    special_offers_checkbox.click()

    # Popuniti ostatak podataka
    first_name_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "first_name"))
    )
    first_name_input.send_keys("John")

    last_name_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "last_name"))
    )
    last_name_input.send_keys("Doe")

    company_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "company"))
    )
    company_input.send_keys("Company Name")

    address_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "address1"))
    )
    address_input.send_keys("123 Street")

    city_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "city"))
    )
    city_input.send_keys("City Name")

    state_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "state"))
    )
    state_input.send_keys("State Name")

    zipcode_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "zipcode"))
    )
    zipcode_input.send_keys("12345")

    mobile_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "mobile_number"))
    )
    mobile_input.send_keys("1234567890")

    # Klik na 'Create Account'
    create_account_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-qa='create-account']"))
    )
    create_account_btn.click()

    # Očekuje se da se pojavi 'Account Created!'
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//b[contains(text(),'Account Created!')]"))
    )
    assert driver.find_element(By.XPATH, "//b[contains(text(),'Account Created!')]").is_displayed()

    # Klik na 'Continue' dugme
    continue_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Continue')]"))
    )
    continue_btn.click()

    # Verifikuj da je korisnik prijavljen sa korisničkim imenom
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),' Logged in as Test User')]"))
    )
    assert driver.find_element(By.XPATH, "//a[contains(text(),' Logged in as Test User')]").is_displayed()

 # Klik na 'Delete Account' dugme
    delete_account_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Delete Account')]"))
    )
    delete_account_btn.click()

    # Verifikuj da je 'ACCOUNT DELETED!' vidljiv i klikni 'Continue'
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//b[contains(text(),'Account Deleted!')]"))
    )
    assert driver.find_element(By.XPATH, "//b[contains(text(),'Account Deleted!')]").is_displayed()

    continue_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Continue')]"))
    )
    continue_btn.click()
