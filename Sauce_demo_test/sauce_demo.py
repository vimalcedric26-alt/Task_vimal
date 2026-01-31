import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
#from webdriver_manager.chrome.import ChromeDriverManager
from selenium.webdriver.common.by import By
#from webdriver_manager.drivers.firefox import GeckoDriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://sauce-demo.myshopify.com")
driver.maximize_window()
driver.find_element(By.XPATH,"//*[@id='customer_login_link']").click()
time.sleep(2)
driver.find_element(By.ID, "customer_email").send_keys("standard_user@gmail.com")
driver.find_element(By.ID, "customer_password").send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@value='Sign In']").click()
time.sleep(2)
print(driver.title)
driver.save_screenshot("sauce.png")
driver.quit()

