import pytest
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("username,password", [
    ("testuser", "wrongpass"),
    ("admin", "admin123"),
])
def test_login_invalid_credentials(driver, username, password):
    driver.get("https://demoqa.com/login")

    username_field = driver.find_element(By.ID, "userName")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login")

    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()

    # Check for error message
    error_message = driver.find_element(By.ID, "name").text
    assert "Invalid username or password!" in error_message
    print(f"Tested with {username}/{password} → {error_message}")
