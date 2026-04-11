from selenium.webdriver.common.by import By


def test_app_starts(driver):
    about_button = driver.find_element(By.ID, "aboutButton")
    assert about_button.is_displayed()