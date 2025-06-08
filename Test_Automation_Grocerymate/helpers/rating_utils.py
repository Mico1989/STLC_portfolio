from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def delete_existing_review(driver):
    try:
        WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='menu-icon']"))
        ).click()
        time.sleep(1)

        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='dropdown-menu']/button[text()='Delete']"))
        ).click()

        # ✅ Rukuj alertom koji pita za potvrdu brisanja
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()

        print("✅ The review has been successfully removed.")
        time.sleep(2)

    except Exception as e:
        print(f"ℹ️ The review was not found or has already been deleted: {str(e)}")

