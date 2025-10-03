from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.maximize_window()
    driver.get("https://demoqa.com/text-box")
    parent_div = driver.find_element(By.XPATH, "//input[@id='userName']/parent::div")
    print(parent_div.get_attribute("class"))
    time.sleep(2)
    driver.get("https://demoqa.com/radio-button")
    radio_button = driver.find_element(By.XPATH, "//input[@id='yesRadio']/following-sibling::label")
    print(radio_button.text)
    driver.get("https://demoqa.com/checkbox")
    plus_button = driver.find_element(By.CSS_SELECTOR, ".rct-option.rct-option-expand-all")
    plus_button.click()
    time.sleep(2)
    following_spans = driver.find_elements(By.XPATH, "//span[text()='Home']/following::span")
    print("Count of following span elements:", len(following_spans))


finally:
    driver.quit
