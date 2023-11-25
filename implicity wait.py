import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait as Ec

service_obj = Service()
driver = webdriver.Chrome(service = service_obj)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR,"input[class='search-keyword']").send_keys("ber")
categories = ["Cucumber - 1 Kg","Raspberry - 1/4 Kg","Strawberry - 1/4 Kg"]

results = driver.find_elements(By.XPATH,"//div[@class = 'product']/h4")
list =[]
for result in results :
    list.append(result.text)

print(list)

assert list ==categories

cart = driver.find_elements(By.XPATH,"//div[@class = 'product']/div/button")
l = []
for i in cart:
    l.append(i.text)
print(l)
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")


sum = 0

for price in prices:
   sum = sum+ int(price.text)

driver.find_element(By.CSS_SELECTOR,"input[class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
time.sleep(10)
wait = WebDriverWait(driver,10)
wait.until(expected_condition.pre(By.CSS_SELECTOR,".promoInfo"))
print(driver.find_element(By.CSS_SELECTOR,"span[class='promoInfo']").text)







