from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def setup():
  driver = webdriver.Chrome()
  driver.get("https://the-internet.herokuapp.com/javascript_alerts")
  return driver

def handling_alerts():
  driver = setup()
  try:
    # Find the first button and click
    btn = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
    btn.click()

    time.sleep(2)  # wait to see the alert
