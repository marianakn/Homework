import time
from selenium.webdriver.common.by import By

def test_click_me_and_radio(driver):
    driver.get("https://demoqa.com/")
    time.sleep(2)
    cards = driver.find_elements(By.CSS_SELECTOR, ".category-cards .card")
    cards[0].click()

    element = driver.find_element(By.ID, "item-4")
    element.click()
    time.sleep(2)

    click_me_button = driver.find_element(By.XPATH, "//button[text()='Click Me']")
    driver.execute_script("arguments[0].scrollIntoView(true);", click_me_button)
    click_me_button.click()

    message = driver.find_element(By.ID, "dynamicClickMessage")
    assert message.is_displayed()
    assert message.text == "You have done a dynamic click"

    driver.switch_to.new_window('tab')
    driver.get("https://demoqa.com/radio-button")
    impressive_label = driver.find_element(By.CSS_SELECTOR, "label[for='impressiveRadio']")
    impressive_label.click()
    impressive_radio = driver.find_element(By.ID, "impressiveRadio")
    assert impressive_radio.is_selected()
