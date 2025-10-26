import time
import pytest
from selenium.webdriver.common.by import By


def test_homework_tasks(driver):
    #Homework1
    driver.get("https://demoqa.com/frames")
    iframe = driver.find_element(By.ID, "frame1")
    driver.execute_script("arguments[0].scrollIntoView();", iframe)
    driver.switch_to.frame(iframe)
    body = driver.find_element(By.TAG_NAME, "body")
    print("Text inside iframe frame1:", body.text)
    driver.switch_to.default_content()
    driver.get("https://demoqa.com/alerts")
    alert_button = driver.find_element(By.ID, "timerAlertButton")
    driver.execute_script("arguments[0].scrollIntoView();", alert_button)
    alert_button.click()
    time.sleep(5)
    alert = driver.switch_to.alert
    print("Alert text:", alert.text)
    alert.accept()

    #homework2
    main_window = driver.current_window_handle
    driver.get("https://demoqa.com/browser-windows")
    driver.switch_to.new_window("tab")
    driver.get("https://demoqa.com/alerts")
    alert = driver.find_element(By.ID, "alertButton")
    alert.click()
    alert = driver.switch_to.alert
    alert.accept()
    driver.switch_to.window(main_window)
    print("Back to main window:", driver.current_url)

    #homework3 - this one sometimes throws error maybe bc of the website?
    # new_window_button = driver.find_element(By.ID, "windowButton")
    # driver.execute_script("arguments[0].scrollIntoView();", new_window_button)
    # new_window_button.click()
    # all_windows = driver.window_handles
    # for handle in all_windows:
    #     if handle != main_window:
    #         driver.switch_to.window(handle)
    #         break
    # message_element = driver.find_element(By.ID, "sampleHeading")
    # driver.execute_script("arguments[0].scrollIntoView();", message_element)
    # message_text = message_element.text
    # print("Message in new window:", message_text)
    # driver.switch_to.window(main_window)
    # print("Switched back to:", main_window)

    #homework4
    driver.get("https://demoqa.com/frames")
    driver.switch_to.frame("frame1")
    text1 = driver.find_element(By.ID, "sampleHeading").text
    print("Text inside frame1:", text1)
    driver.switch_to.default_content()
    driver.switch_to.frame("frame2")
    text2 = driver.find_element(By.ID, "sampleHeading").text
    print("Text inside frame2:", text2)
    driver.switch_to.default_content()
    print("Iframe task completed")

    #homework5
    driver.get("https://demoqa.com/alerts")
    alert = driver.find_element(By.ID, "alertButton")
    alert.click()
    alert = driver.switch_to.alert
    alert.dismiss()
    prompt_button = driver.find_element(By.ID, "promtButton")
    prompt_button.click()
    prompt_alert = driver.switch_to.alert
    prompt_alert.send_keys("Mariana")
    prompt_alert.accept()
    result_text = driver.find_element(By.ID, "promptResult").text
    print("Result message:", result_text)
