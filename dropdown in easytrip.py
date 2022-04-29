from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s=Service('C:\\chromedriver')
driver=webdriver.Chrome(service=s)
driver.get("https://www.easemytrip.com/?utm_campaign=740105751&utm_source=g_c&utm_medium=cpc&utm_term=e_flight%20booking&adgroupid=129016364612&gclid=CjwKCAiAgbiQBhAHEiwAuQ6BkrAxPR6H0-87JV6pUAauhWFAZevO5ugNoYthvkqLUcof7YFiqx914BoC9A8QAvD_BwE")


print(driver.find_element(By.XPATH,("(//span[@class='drpNoTrv'])[1]")).text)
driver.find_element(By.XPATH,("(//span[@class='drpNoTrv'])[1]")).click()
print(driver.find_element(By.XPATH,("(//div[@class='ttl_col'])[1]/p")).text)
print(driver.find_element(By.XPATH,("(//div[@class='ttl_col'])[2]/p")).text)
print(driver.find_element(By.XPATH,("(//div[@class='ttl_col'])[3]/p")).text)
#driver.find_element(By.XPATH,("(//input[@class='plus_boxChd'])[1]")).click()
a=7
while a>=0:
    driver.find_element(By.XPATH, ("(//input[@class='plus_boxChd'])[1]")).click()

    a-=1
driver.find_element(By.XPATH,("(//input[@class='plus_box1Inf'])[1]")).click()
driver.find_element(By.ID,("traveLer")).click()
driver.find_element(By.ID,("FromSector_show")).clear()
driver.find_element(By.ID,("FromSector_show")).send_keys("Bangalore")
print(driver.title)
print(driver.current_url)
a=driver.find_element(By.XPATH,("//div[@class='middle_sec']/h1")).text
print(a)
driver.get("https://www.easemytrip.com/bus/")
driver.find_element(By.ID,("txtSrcCity")).send_keys(a)