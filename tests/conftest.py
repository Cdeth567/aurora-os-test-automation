# conftest.py
import pytest
from appium import webdriver
from appium.options.common import AppiumOptions


@pytest.fixture(scope="session")
def driver():
    appium_server_url = f'http://localhost:4723'
    
    appium_server_capabilities = {
        "automationName": "Aurora",
        'platformName': 'Aurora',
        'platformVersion': '2.2',
        'newCommandTimeout': 86400,
        'appPackage': 'ru.auroraos.ApplicationTemplate',
        'deviceName': '192.168.2.15',
        'autoLaunch': False,
        'appiumInspector': False,
    }

    appium_driver_options = AppiumOptions().load_capabilities(appium_server_capabilities)

    driver = webdriver.Remote(
        appium_server_url,
        options=appium_driver_options
    )

    driver.launch_app()

    yield driver
    driver.quit()