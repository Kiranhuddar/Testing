from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

serice_obj = Service()
driver = webdriver.Chrome(service=serice_obj)
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH,"//a[text() = 'Shop']").click()

#xpath = //a[contains(@href,'shop')]  regular expression a[href* = 'shop']
products = driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for product in products :
    productname = product.find_element(By.XPATH,"div/h4/a").text
    if productname == 'Blackberry':
        product.find_element(By.XPATH,"div/button").click()



driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()

driver.find_element(By.CSS_SELECTOR,"button[class='btn btn-success']").click()

driver.find_element(By.ID,"country").send_keys("India")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_all_elements_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,'India').click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()

success_message = driver.find_element(By.XPATH,"//div[@class='alert alert-success alert-dismissible']").text
print(success_message)
assert "Success! Thank you! Your order will be delivered in next few weeks :-)."  success_message

