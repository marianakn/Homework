from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.remote.webelement import WebElement

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/")
    time.sleep(2)
    cards = driver.find_elements(By.CSS_SELECTOR, ".category-cards .card")
    cards[0].click()
    element = driver.find_element(By.ID,  "item-4")
    element.click()
    time.sleep(2)
    click_me_button = driver.find_element(By.XPATH, "//button[text()='Click Me']")
    driver.execute_script("arguments[0].scrollIntoView(true);", click_me_button)
    time.sleep(1)
    click_me_button.click()
    message = driver.find_element(By.ID, "dynamicClickMessage")
    assert message.is_displayed(), "Message is not displayed!"
    assert message.text == "You have done a dynamic click", "Message text does not match!"
    print("Verification passed:", message.text)

    driver.switch_to.new_window('tab')
    driver.get("https://demoqa.com/radio-button")
    current_url = driver.current_url

    impressive_label = driver.find_element(By.CSS_SELECTOR, "label[for='impressiveRadio']")
    driver.execute_script("arguments[0].scrollIntoView(true);", impressive_label)
    time.sleep(1)
    impressive_label.click()

    impressive_radio = driver.find_element(By.ID, "impressiveRadio")
    assert impressive_radio.is_selected(), "'Impressive' radio button was not selected!"
    print("'Impressive' radio button clicked successfully!")

    time.sleep(2)


finally:
    driver.quit()