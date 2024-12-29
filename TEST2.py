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
        driver.get("https://www.example.com")  # Replace with the URL of the web page

        # Locate the search box (update the selector to match your target site)
        search_box = driver.find_element(By.NAME, "New York")  # Example uses 'name="New York"'

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

