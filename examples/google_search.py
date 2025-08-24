from selenium import webdriver
from selenium.webdriver.common.By import By
from selenium.webdriver.common.Keys import Keys
import time

# Initialize Chrome
def setup():
  driver = webdriver.Chrome()
  return driver

# Waiting for 3s to show results before closing the browser and also printing the page title
def teardown():
time.sleep(3)
print("Page Title is:", driver.title)
driver.quit()

def search():
  try:
    driver = setup()
    driver.get("https://www.google.com")
    # Find the search box and type a query
    search_box = driver.find_element(BY.NAME,"q")
    search_box.send_keys("Selenium Python")
    # Hits the enter key on your keyboard
    search_box.send_keys(Keys.RETURN)

  finally:
    teardown()

if __name__ == "__main__":
  search()
