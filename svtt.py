Design and implement Selenium environment setup to configure WebDriver and verify browser.from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome driver automatically
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open website
driver.get("https://www.google.com")

# Maximize window
driver.maximize_window()

# Wait
time.sleep(3)

# Verify
print("Page Title is:", driver.title)

if "Google" in driver.title:
    print("Browser launched successfully ")
else:

    code 2 Design and implement basic browser navigation to automate opening, refreshing, and navigating pages.
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open first website
driver.get("https://www.google.com")
print("Opened Google")
time.sleep(2)

# Navigate to another page
driver.get("https://www.wikipedia.org")
print("Opened Wikipedia")
time.sleep(2)

# Go back
driver.back()
print("Navigated Back")
time.sleep(2)

# Go forward
driver.forward()
print("Navigated Forward")
time.sleep(2)

# Refresh page
driver.refresh()
print("Page Refreshed")
time.sleep(2)

# Close browser
driver.quit()

code 3 Design and implement locators to find web elements using ID, XPath, or CSS selectors.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open website (example login page)
driver.get("https://www.facebook.com")

driver.maximize_window()
time.sleep(2)

# ----------- LOCATORS -----------

# 1. Using ID
username = driver.find_element(By.ID, "email")
username.send_keys("your_email")

# 2. Using CSS Selector
password = driver.find_element(By.CSS_SELECTOR, "input[name='pass']")
password.send_keys("your_password")

# 3. Using XPath
login_btn = driver.find_element(By.XPATH, "//button[@name='login']")
login_btn.click()

time.sleep(3)

# Close browser
driver.quit()

code 4 Design and implement form automation to fill and submit forms with test data.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open demo form website
driver.get("https://demoqa.com/text-box")

driver.maximize_window()
time.sleep(2)

# ----------- FILL FORM -----------

# Name
driver.find_element(By.ID, "userName").send_keys("Gauri Dani")

# Email
driver.find_element(By.ID, "userEmail").send_keys("gauri@gmail.com")

# Current Address
driver.find_element(By.ID, "currentAddress").send_keys("Aurangabad")

# Permanent Address
driver.find_element(By.ID, "permanentAddress").send_keys("Maharashtra")

time.sleep(2)

# ----------- SUBMIT FORM -----------

driver.find_element(By.ID, "submit").click()

time.sleep(3)

# ----------- VERIFY OUTPUT -----------

try:
    output_name = driver.find_element(By.ID, "name").text
    print("Form Submitted Successfully ")
    print(output_name)
except:
    print("Form Submission Failed ")

# Close browser
driver.quit()

code5 Design and implement dropdown and checkbox handling using Select and click methods.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time

# Launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open demo page
driver.get("https://demoqa.com/select-menu")

driver.maximize_window()
time.sleep(2)

# ----------- DROPDOWN HANDLING -----------

# Locate dropdown
dropdown = driver.find_element(By.ID, "oldSelectMenu")

# Create Select object
select = Select(dropdown)

# Select by visible text
select.select_by_visible_text("Blue")
time.sleep(2)

# Select by value
select.select_by_value("4")  # Purple
time.sleep(2)

# Select by index
select.select_by_index(2)
time.sleep(2)

# ----------- CHECKBOX HANDLING -----------

# Open checkbox page
driver.get("https://demoqa.com/checkbox")
time.sleep(2)

# Click checkbox
checkbox = driver.find_element(By.XPATH, "//span[@class='rct-checkbox']")
checkbox.click()
time.sleep(2)

# Verify checkbox selected
if checkbox.is_displayed():
    print("Checkbox selected ")
else:
    print("Checkbox not selected ")

# Close browser
driver.quit()

code 6 Design and implement alert and pop-up handling to interact with JavaScript alerts.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open demo alerts page
driver.get("https://demoqa.com/alerts")

driver.maximize_window()
time.sleep(2)

# ----------- SIMPLE ALERT -----------

# Click button to trigger alert
driver.find_element(By.ID, "alertButton").click()
time.sleep(2)

# Switch to alert
alert = driver.switch_to.alert

print("Alert Text:", alert.text)

# Accept alert
alert.accept()
time.sleep(2)

# ----------- CONFIRM ALERT -----------

driver.find_element(By.ID, "confirmButton").click()
time.sleep(2)

alert = driver.switch_to.alert
print("Confirm Alert:", alert.text)

# Dismiss alert
alert.dismiss()
time.sleep(2)

# ----------- PROMPT ALERT -----------

driver.find_element(By.ID, "promtButton").click()
time.sleep(2)

alert = driver.switch_to.alert

# Send input
alert.send_keys("Hello Gauri")

# Accept prompt
alert.accept()
time.sleep(2)

# Close browser
driver.quit()

code 7 Design and implement screenshot capturing to save images of web pages during testing.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open website
driver.get("https://www.google.com")

driver.maximize_window()
time.sleep(2)

# ----------- TAKE SCREENSHOT -----------

# Save screenshot
driver.save_screenshot("google_page.png")

print("Screenshot saved successfully ✅")

time.sleep(2)

# Close browser
driver.quit()

code8 Design and implement mouse and keyboard actions using the Actions class for advanced interactions.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open demo page
driver.get("https://demoqa.com/buttons")

driver.maximize_window()
time.sleep(2)

# Create Actions object
actions = ActionChains(driver)

# ----------- MOUSE ACTIONS -----------

# Double Click
double_btn = driver.find_element(By.ID, "doubleClickBtn")
actions.double_click(double_btn).perform()
print("Double Click performed")

time.sleep(2)

# Right Click
right_btn = driver.find_element(By.ID, "rightClickBtn")
actions.context_click(right_btn).perform()
print("Right Click performed")

time.sleep(2)

# ----------- KEYBOARD ACTIONS -----------

# Open another page for keyboard input
driver.get("https://demoqa.com/text-box")
time.sleep(2)

# Locate input field
name_field = driver.find_element(By.ID, "userName")

# Type text
actions.send_keys_to_element(name_field, "Gauri Dani").perform()
time.sleep(2)

# Select all text (CTRL + A)
actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
time.sleep(2)

# Copy text (CTRL + C)
actions.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
time.sleep(2)

print("Keyboard actions performed")

# Close browser
driver.quit()

code 9 Design and implement web table interaction to extract and process data from table elements.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open demo table page
driver.get("https://demoqa.com/webtables")

driver.maximize_window()
time.sleep(3)

# ----------- EXTRACT TABLE DATA -----------

# Get all rows
rows = driver.find_elements(By.XPATH, "//div[@class='rt-tr-group']")

print("Table Data:\n")

for row in rows:
    # Get all columns in each row
    cols = row.find_elements(By.XPATH, ".//div[@class='rt-td']")
    
    # Extract text from each column
    row_data = [col.text for col in cols]
    
    # Print row data if not empty
    if any(row_data):
        print(row_data)


print("\nFiltered Data (Age > 25):")

for row in rows:
    cols = row.find_elements(By.XPATH, ".//div[@class='rt-td']")
    if len(cols) > 2 and cols[2].text.isdigit():
        if int(cols[2].text) > 25:
            print([col.text for col in cols])

# Close browser
driver.quit()

code 10 Design and implement wait mechanisms to handle dynamic web elements using implicit or explicit waits.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Launch browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Apply implicit wait (10 seconds)
driver.implicitly_wait(10)

# Open website
driver.get("https://demoqa.com/dynamic-properties")

driver.maximize_window()

# Element appears after delay
button = driver.find_element("id", "visibleAfter")
button.click()

print("Clicked using Implicit Wait")

driver.quit()