import time
from selenium import webdriver

def test_armstqb_chrome(driver):
    driver.get("https://www.armstqb.org/")
    assert "ArmSTQB" in driver.title
    driver.switch_to.new_window('tab')
    driver.get("https://www.armstqb.org/partners")
    assert "partners" in driver.current_url

def test_armstqb_safari():
    driver = webdriver.Safari()
    try:
        driver.get("https://www.armstqb.org")
        assert "ArmSTQB" in driver.title
        driver.switch_to.new_window('tab')
        driver.get("https://www.armstqb.org/partners")
        assert "partners" in driver.current_url
    finally:
        driver.quit()
