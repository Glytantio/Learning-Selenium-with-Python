from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def setup():
  driver = webdriver.Chrome()
  return driver

def pressOK():
  # This function is for pressing the ok button whenever an alert is displayed
  alert = driver.switch_to.alert
  print = ("Alert text:", alert.text)
  alert.accept()
  
# Waiting for 3s to show results before closing the browser and also printing the page title
def teardown():
time.sleep(3)
print("Page Title is:", driver.title)
driver.quit()

def handling_alerts():
  driver = setup()
  try:
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    # Find the first button and click
    btn = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
    btn.click()
    
    time.sleep(2)  # wait to see the alert
    
    pressOK() # Calls the function to click the ok button for every alert

    # Find the second button and click
    btn2 = driver.find_element(BY.XPATH, "//button[text()='Click for JS Alert']")
    btn2.click()

    time.sleep(2)

    pressOK()
    
    # Find the third button and click
    btn3 = driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']")
    btn3.click()

    time.sleep(2)
    
    alert = driver.switch_to.alert
    print = ("Alert text:", alert.text)
    # Type something inside the confirm alert and enters it.
    alert.send_keys("Hello Glytantio!")
    alert.accept()

  finally:
    # Closes the browser
    teardown()

if __name__ == "__main__":
  # Initiate the automation script
  handling_alerts()
  
