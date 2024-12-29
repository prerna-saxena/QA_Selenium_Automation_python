from selenium import webdriver
from selenium.webdriver.common.keys import keys
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
diver.get("http://www.python.org")
assert "Python" in driver.title
elem= driver.find_element(By.NAME, "q")
elem.clear()
elem.send_Keys("pycon")
elem.send_Keys(Keys.RETURN)
assert "no result found" not in driver.page_source
time.sleep(6)
driver.close()















