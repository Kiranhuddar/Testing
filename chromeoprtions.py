from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(service= service_obj,options=chrome_options)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
print(driver.title)
