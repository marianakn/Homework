from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--start-maximized")
options.add_argument("--incognito")
options.add_argument("/Users/<marianakn>/Library/Application Support/Google/Chrome")
options.add_argument("profile-directory=Profile 2")

driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()

#task1
try:
    driver.get("https://demoqa.com/dynamic-properties")
    driver.implicitly_wait(10)
    enable_button = driver.find_element(By.ID, "enableAfter")
    enable_button.click()
    print("Button clicked successfully.")
except Exception as e:
    print(" Could not click the button:", e)

#task2
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    start_button = driver.find_element(By.XPATH, "//div[@id='start']/button")
    start_button.click()

    wait = WebDriverWait(driver, 15)
    text_element = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//div[@id='finish']/h4"))
    )
    print(text_element.text)

#task3
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    button = driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']")
    button.click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()

#task4
    driver.get("https://demoqa.com/automation-practice-form")
    element = driver.find_element(By.CSS_SELECTOR, ".hidden_button")
    element.click()
    print("Element found:", element.text)
except NoSuchElementException:
    print("Element with ID 'ghostButton' was not found on the page.")


finally:
    driver.quit()