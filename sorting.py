from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
browsersorterlist = []
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

driver.find_element(By.XPATH,"//span[text() ='Veg/fruit name']").click()

veggieelements = driver.find_elements(By.XPATH,"//tr/td[1]")

for veggieelement in veggieelements:
    browsersorterlist.append(veggieelement.text)
orginal_sorted_list = browsersorterlist.copy()

browsersorterlist.sort()

assert browsersorterlist == orginal_sorted_list







