from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service = service_obj)
driver.get("https://rahulshettyacademy.com/client/auth/login")
driver.find_element(By.XPATH,"//a[@class ='forgot-password-link']").click()
driver.find_element(By.XPATH,"//form/div[1]/input[@type='email']").send_keys('huddarkiran@gmail.com')
driver.find_element(By.CSS_SELECTOR,"input[type = 'password']").send_keys('Kiran')
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Confirm Passsword' ]").send_keys('kiran')
driver.find_element(By.XPATH,"//button[@class='btn btn-custom btn-block']").click()

