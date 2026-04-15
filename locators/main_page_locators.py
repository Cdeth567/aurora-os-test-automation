from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_PAGE = (By.XPATH, "//*[@objectName='mainPage']")
    TITLE = (By.XPATH, "//*[@text='Call API DBus']")
    SPINNER = (
        By.XPATH,
        "//*[contains(@id, 'AnimatedLoader') "
        "or contains(@id, 'Loader') "
        "or contains(@id, 'Busy') "
        "or contains(@id, 'Spinner')]",
    )
    OUTGOING_CALL_BUTTON = (
        By.XPATH,
        "//*[@objectName='outgoingCallButton' or @text='Исходящий вызов']",
    )
    INCOMING_CALL_BUTTON = (
        By.XPATH,
        "//*[@objectName='incomingCallButton' or @text='Входящий вызов']",
    )