from selenium.webdriver.common.by import By


class CallPageLocators:
    CONNECTION_TEXT = (By.XPATH, "//*[contains(@text, 'Соединение')]")
    REMOTE_NAME_TEXT = (By.XPATH, "//*[contains(@text, 'Remote name')]")
    DROP_CALL_BUTTON = (
        By.XPATH,
        "//*[contains(@id, 'drop') "
        "or contains(@id, 'hang') "
        "or contains(@text, 'Сброс') "
        "or contains(@text, 'Заверш')]",
    )