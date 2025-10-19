import time
from selenium.webdriver.common.by import By

def test_textbox_elements(driver):
    driver.get("https://demoqa.com/text-box")
    parent_div = driver.find_element(By.XPATH, "//input[@id='userName']/parent::div")
    assert parent_div.get_attribute("class") is not None

    time.sleep(1)
    driver.get("https://demoqa.com/radio-button")
    radio_button = driver.find_element(By.XPATH, "//input[@id='yesRadio']/following-sibling::label")
    assert radio_button.text == "Yes"

    driver.get("https://demoqa.com/checkbox")
    plus_button = driver.find_element(By.CSS_SELECTOR, ".rct-option.rct-option-expand-all")
    plus_button.click()
    time.sleep(2)
    following_spans = driver.find_elements(By.XPATH, "//span[text()='Home']/following::span")
    assert len(following_spans) > 0
