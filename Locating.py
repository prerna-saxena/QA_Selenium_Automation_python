from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the web driver
def main():
    # Path to  WebDriver (e.g., ChromeDriver path)
    driver_path = "path/to/chromedriver"
    driver = webdriver.Chrome(executable_path=driver_path)

    try:
        
        driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo") 

        # Locate the search box (update the selector to match your target site)
        search_box = driver.find_element(By.NAME, "q")  # Example uses 'name="q"'

        # Interact with the search box
        search_box.clear()
        search_box.send_keys("New York")
        search_box.send_keys(Keys.RETURN)  # Simulate pressing 'Enter'

        # Optional: Wait for the results to load
        time.sleep(5)  # Adjust the wait time as needed

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        driver.quit()
