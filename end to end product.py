import time

from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

s = Service("C:\\chromedriver")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR,("a[href*=shop]")).click()
products=driver.find_elements(By.XPATH, ("//div[@class='card h-100']"))
print(len(products))
#index = 0
#while index < len(products):
    #print(products[index].text)
    #if products[index].text=="Blackberry":
        #index, driver.find_elements(By.XPATH, ("//div[@class='card-footer']/button"))[index].click()
    #index+=1

for product in products:
    pro_name=product.find_element(By.XPATH,("div/h4/a")).text
    if pro_name=='Blackberry':
        product.find_element(By.XPATH,("div/button")).click()


driver.find_element(By.XPATH,("//a[@class='nav-link btn btn-primary']")).click()

order=driver.find_element(By.LINK_TEXT,("Blackberry")).text
print(order)

assert order=="Blackberry"

checkout= driver.find_element(By.XPATH,("//button[@class='btn btn-success']"))
checkout.click()
countries=driver.find_element(By.ID,("country")).send_keys("ind")
wait=WebDriverWait(driver,8)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,("India")).click()
driver.find_element(By.XPATH,("//div[@class='checkbox checkbox-primary']")).click()
driver.find_element(By.XPATH,("//input[@class='btn btn-success btn-lg']")).click()
#succ=(driver.find_element(By.XPATH,("//div[@class='alert alert-success alert-dismissible']")).text




s = Service("C:\\chromedriver")
driver = webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.CSS_SELECTOR,("a[href*=shop]")).click()
products=driver.find_elements(By.XPATH, ("//div[@class='card h-100']"))
print(len(products))