
#creating driver
from selenium import webdriver
driver = webdriver.Chrome()

try:
    driver.get("http://google.com")
    current_url = driver.current_url
    print("Current URL", current_url)
    current_title = driver.title
    print("Current title", current_title)

    assert "Python" in current_title
    print("Current title", current_title)

finally: quit()