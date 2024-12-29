import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome()
query= "New York"
file=0
#for i in range(1, 20):
driver.get(f"https://www.lambdatest.com/selenium-playground/table-sort-search-{query}&pages={i}")

elem= driver.find_element(By.CLASS_NAME, "puis-card-container")
print(f"{len(elems)} items found)

for elem in elems:
   d= elem.get_attribute("outerHTML")
   wih open("data/{query}_{file}.html", "w", encoding="utf-8") as f:
   f.write(d)
   file+=1
   print(elem.text)
#print(elem.get_attribute("outerHTML"))
#print(elem.text)
time.sleep(4)
driver.close()
