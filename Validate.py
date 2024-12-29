from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the web driver
def main():
    # Path to your WebDriver (e.g., ChromeDriver path)
    driver_path = "path/to/chromedriver"
    driver = webdriver.Chrome(executable_path=driver_path)

    try:
        # Open the desired web page
        driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo") 
        # Locate the search box (update the selector to match your target site)
        search_box = driver.find_element(By.NAME, "q")  # Example uses 'name="q"'

        # Interact with the search box
        search_box.clear()
        search_box.send_keys("New York")
        search_box.send_keys(Keys.RETURN)  # Simulate pressing 'Enter'

        # Optional: Wait for the results to load
        time.sleep(5)  # Adjust the wait time as needed

        # Validate the search results
        results = driver.find_elements(By.CLASS_NAME, "result-entry")  # Replace with the actual class for result entries
        total_results_text = driver.find_element(By.ID, "total-results").text  # Replace with the actual ID or selector for total results

        # Check the number of displayed results and total entries
        if len(results) == 5 and "24" in total_results_text:
            print("Test passed: 5 entries are displayed out of 24 total entries.")
        else:
            print(f"Test failed: Found {len(results)} entries, expected 5. Total results: {total_results_text}")



    finally:
        # Close the browser
        driver.close()


