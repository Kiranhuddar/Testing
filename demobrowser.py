from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#chrome driver - chrome browser
service_obj = Service()
# driver = webdriver.Chrome(service=service_obj)
# driver.maximize_window()
# driver.get('https://rahulshettyacademy.com')
# print(driver.title)
# driver.get('https:\\www.flipkart.com')
# #driver.minimize_window()
# driver.back()
# driver.refresh()
# driver.forward()
# print(driver.current_url)


#for firefox
# driver = webdriver.Edge(service = service_obj)
# driver.get('https://rahulshettyacademy.com/angularpractice/')
# print(driver.title)
# driver.find_element(By.NAME,'email').send_keys('huddarkiran@gmail.com')
# driver.find_element(By.ID,'exampleInputPassword1').send_keys('123456')
# driver.find_element(By.ID,'exampleCheck1').click()

driver = webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.find_element(By.NAME,'email').send_keys('huddarkiran@gmail.com')
driver.find_element(By.ID,'exampleInputPassword1').send_keys('Kiran')
driver.find_element(By.ID,'exampleCheck1').click()
dropdown = Select(driver.find_element(By.ID,'exampleFormControlSelect1'))
dropdown.select_by_index(0)

dropdown.select_by_visible_text("Female")

driver.find_element(By.XPATH,"//input[@type = 'submit']").click()
message = driver.find_element(By.CLASS_NAME,'alert-success').text
print(message)

driver.find_element(By.CSS_SELECTOR,"input[name = 'name']").send_keys('Kiran')

assert 'Success' in message

driver.find_element(By.XPATH,'/html/body/app-root/form-comp/div/h4/input').send_keys('hello')

