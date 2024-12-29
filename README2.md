way to Run the Script
Install Dependencies: Ensure Python (>=3.7) is installed in system. 
Then install the required Python packages:

pip install selenium pytest webdriver-manager


Set Up WebDriver: The script uses webdriver-manager to manage the Chrome WebDriver automatically.

Run the Test: Execute the test using pytest:

pytest qa_selenium_test.py


Output:

The test outputs results to the console.
Any assertion failure will display a descriptive error message.
