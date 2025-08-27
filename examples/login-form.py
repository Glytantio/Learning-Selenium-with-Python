
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def setup_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver


def login_test():
    driver = setup_browser()

    try:
        driver.get("https://practicetestautomation.com/practice-test-login/")
      
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")
      
        username.send_keys("student")
        password.send_keys("Password123")

        login_button = driver.find_element(By.ID, "submit")
        login_button.click()

        time.sleep(3)

        print("Page title after login is:", driver.title)

    finally:
        driver.quit()


if __name__ == "__main__":
    login_test()
