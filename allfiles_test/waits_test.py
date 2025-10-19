import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException

def test_dynamic_button_click(driver):
    driver.get("https://demoqa.com/dynamic-properties")
    driver.implicitly_wait(10)
    enable_button = driver.find_element(By.ID, "enableAfter")
    enable_button.click()

def test_dynamic_loading(driver):
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
    driver.find_element(By.XPATH, "//div[@id='start']/button").click()
    wait = WebDriverWait(driver, 15)
    text_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='finish']/h4")))
    assert text_element.text == "Hello World!"

def test_js_alert(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    assert "I am a JS Alert" in alert.text
    alert.accept()

@pytest.mark.xfail(reason="Element intentionally missing")
def test_hidden_button(driver):
    driver.get("https://demoqa.com/automation-practice-form")
    element = driver.find_element(By.CSS_SELECTOR, ".hidden_button")
    element.click()
