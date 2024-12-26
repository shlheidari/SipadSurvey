from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup constants and configuration
TIMEOUT = 60
LOGIN_URL = "https://sipad.tums.ac.ir/Dashboard"

# Input credentials and preferences
username = input("Enter your username: ")
password = input("Enter your password: ")
print("Please select the corresponding number to indicate your preferred option:\n"
      "0: very good\n1: good\n2: average\n3: weak\n4: very weak\n5: undecided\n(Default Response: 0)")
try:
    opt = int(input("Enter the corresponding number: "))
    if opt not in range(6):
        opt = 0
except ValueError:
    opt = 0

print("The initial startup process may require some time.")

# Initialize the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, TIMEOUT)

def switch_to_frame(xpath_or_id, by=By.XPATH):
    """Switch to an iframe identified by XPath or ID."""
    iframe = wait.until(EC.presence_of_element_located((by, xpath_or_id)))
    driver.switch_to.frame(iframe)

def click_element(xpath):
    """Wait and click an element identified by XPath."""
    element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    element.click()

def fill_field(xpath, value):
    """Wait for a field and fill it with a value."""
    field = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    field.send_keys(value)

# Open the website and login
driver.get(LOGIN_URL)
switch_to_frame("/html/body/div[1]/div/div/app-root/app-main/div/app-dashboard/mat-sidenav-container/mat-sidenav-content/div/div[2]/div/iframe")
click_element("/html/body/div[1]/div/div/app-root/app-profile-public/div/app-public/mat-sidenav-container/mat-sidenav-content/div/div/div[2]/mat-list[1]/div/mat-grid-list/div/mat-grid-tile[1]")
driver.switch_to.default_content()
switch_to_frame("/html/body/div[1]/div/div/app-root/app-main/div/app-dashboard/mat-sidenav-container/mat-sidenav-content/div/div[2]/div/iframe[2]")

# Fill in login credentials
fill_field("/html/body/div[1]/div/div/app-root/app-singin/div/app-singin-user/div/div/div[2]/form/div[1]/div[2]/div/mat-card-content/p[1]/mat-form-field/div/div[1]/div/input", username)
fill_field("/html/body/div[1]/div/div/app-root/app-singin/div/app-singin-user/div/div/div[2]/form/div[1]/div[2]/div/mat-card-content/p[2]/mat-form-field/div/div[1]/div[1]/input", password)
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/app-root/app-singin/div/app-singin-user/div/div/div[2]/form/div[1]/div[2]/div/mat-card-content/p[2]/mat-form-field/div/div[1]/div[1]/input").send_keys(Keys.RETURN)

# Navigate to survey
driver.switch_to.default_content()
switch_to_frame("iframe_-1", By.ID)
click_element("/html/body/form/div[5]/div/div/table/tbody/tr/td[7]/input")
driver.switch_to.default_content()
switch_to_frame("iframe_New_EvalAnswerSubject1_Tab", By.ID)

# Process survey responses
all_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/form/div[5]/div/div/table/tbody/*")))

for _ in range(len(all_elements)):
    while True:
        try:
            driver.switch_to.default_content()
            switch_to_frame("iframe_New_EvalAnswerSubject1_Tab", By.ID)
            click_element("/html/body/form/div[5]/div/div/table/tbody/tr[1]/td[12]/input")
            driver.switch_to.default_content()
            switch_to_frame("iframe_New_EvalAnswerListItem_Tab", By.ID)
            
            elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, f"//input[starts-with(@id, 'rb{opt}')]")))
            for element in elements:
                element.click()
            
            click_element("/html/body/form/div[3]/input")
            break
        except Exception:
            pass

# Close the browser
driver.quit()
print("Enjoy!")
