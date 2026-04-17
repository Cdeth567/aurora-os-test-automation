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
        "//*[@objectName='incomingCallButton' or @text='Входящий вызов' or contains(@text, 'Входящий вызов (')]",
    )
    CALLS = (By.XPATH, "//*[@text='Звонки']")
    FUNCTIONS = (By.XPATH, "//*[@text='Функции']")
    
    HOLDING_SWITCH = (By.XPATH, "//TextSwitch[@text='Удержание']")
    HOLDING_TITLE = (By.XPATH, "//LabelBase[@text='Удержание']")
    HOLDING_DESCRIPTION = (By.XPATH, "//*[@text='Вкл/Выкл удержания звонка']")

    DTMF_SWITCH = (By.XPATH, "//TextSwitch[@text='DTMF']")
    DTMF_TITLE = (By.XPATH, "//LabelBase[@text='DTMF']")
    DTMF_DESCRIPTION = (By.XPATH, "//*[@text='Вкл/Выкл DTMF (поддержка цифровой клавиатуры)']")
    DTMF_PLACEHOLDER = (By.XPATH, "//*[@text='Текст DTMF']")
    INCOMING_COUNTDOWN = (By.XPATH, "//*[contains(@text, 'Входящий вызов (')]")
