

from selenium import webdriver
import time #this is for safari
driver = webdriver.Chrome()

try:
    driver.get("https://www.armstqb.org/")
    driver.maximize_window()
    current_url = driver.current_url
    print("Current URL", current_url)
    current_title = driver.title
    print("Current title", current_title)
    driver.switch_to.new_window('tab')
    driver.get("https://www.armstqb.org/partners")
    current_url = driver.current_url
    print("Current URL:", current_url)
    driver.close()
    driver.minimize_window()
    time.sleep(2)

finally: quit()

#created separate as the setting are different
driver = webdriver.Safari()
try:
    driver.get("https://www.armstqb.org")
    driver.set_window_size(1920, 1080)
    expected_title = "ArmSTQB"
    actual_title = driver.title
    print("Page title:", actual_title)
    driver.switch_to.new_window('tab')
    driver.get("https://www.armstqb.org/partners")
    current_url = driver.current_url
    print("Current URL:", current_url)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.set_window_size(300, 300)
    time.sleep(2)

finally:
    driver.quit()