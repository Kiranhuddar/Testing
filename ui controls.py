import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
service_obj =Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
options = driver.find_elements(By.XPATH,"//input[@type ='checkbox']")
for option in options:
    if option.get_attribute('value') == 'option2':
        option.click()
        assert option.is_selected()

radio_buttons =driver.find_elements(By.CSS_SELECTOR,"input[class='radioButton']")
for radio_button in radio_buttons:
    if radio_button.get_attribute('value')=='radio2':
        radio_button.click()
        assert radio_button.is_selected()

driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,'hide-textbox').click()
assert driver.find_element(By.ID,"displayed-text").is_displayed()


