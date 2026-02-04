
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(service = Service(GeckoDriverManager().install()))
driver.get('https://www.guvi.in/courses/?current_tab=paidcourse')
labels = driver.find_elements(By.XPATH,"//ul//child::div/input[@type='checkbox'][1]")
for label in labels:
    print(label.text)

print(driver.title)


