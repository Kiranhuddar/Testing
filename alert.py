import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
service_obj =Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.ID,"name").send_keys("Kiran")
driver.find_element(By.ID,"confirmbtn").click()
alert = driver.switch_to.alert
print(alert.text)
assert "Kiran" in alert.text

alert.accept()