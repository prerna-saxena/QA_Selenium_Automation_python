import pytest
from selenium import webdriver
from selenium.web
driver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Test URL for Selenium Playground
URL = "https://www.seleniumeasy.com/test/table-search-filter-demo.html"

@pytest.fixture(scope="module")
def setup_browser():
    """Setup the browser instance."""
    # Initialize the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_table_search_functionality(setup_browser):
    """Test the table search functionality on Selenium Playground."""
    driver = setup_browser

    # Navigate to the URL
    driver.get(URL)

    # Locate the search input box
    search_box = driver.find_element(By.ID, "task-table-filter")

    # Input search term "New York"
    search_term = "New York"
    search_box.clear()
    search_box.send_keys(search_term)

    # Verify results match the search term
    rows = driver.find_elements(By.XPATH, "//table[@id='task-table']/tbody/tr")
    visible_rows = [row for row in rows if row.is_displayed()]

    # Check if 5 rows are displayed
    assert len(visible_rows) == 5, f"Expected 5 entries, but found {len(visible_rows)}."

    # Validate that the total table entries remain 24
    all_rows = driver.find_elements(By.XPATH, "//table[@id='task-table']/tbody/tr")
    assert len(all_rows) == 24, "Total table entries should be 24."

    # Validate that all displayed rows contain the search term "New York"
    for row in visible_rows:
        assert search_term in row.text, f"Search term '{search_term}' not found in row: {row.text}"
