from selenium import webdriver
from selenium.webdriver.common.By import By
from selenium.webdriver.common.Keys import Keys
import time

def setup():
  driver = webdriver.Chrome()
  driver.get("https://www.google.com")
  assert "Google" in driver.title

def teardown():
time.sleep(3)
print("Page Title is:", driver.title)
driver.quit()

setup()
search_box = driver.find_element(BY.NAME,"q")
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.RETURN)
teardown()
