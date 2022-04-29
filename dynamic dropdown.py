import time

from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s=Service("C:\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,("autosuggest")).send_keys("ind")
time.sleep(10)
countries=driver.find_elements(By.CSS_SELECTOR,("li[class='ui-menu-item'] a"))
print(len(countries))
for country in countries:
    if country.text =="India":
        country.click()
assert driver.find_element(By.ID,("autosuggest")).get_attribute('value')=='India'

assert driver.find_element(By.ID,("autosuggest")).get_attribute('value')=='India'
driver=webdriver.Chrome(service=s)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,("autosuggest")).send_keys("ind")
time.sleep(10)
countries=driver.find_elements(By.CSS_SELECTOR,("li[class='ui-menu-item'] a"))
print(len(countries))
