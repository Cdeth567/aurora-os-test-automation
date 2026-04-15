import pytest
from appium import webdriver
from appium.options.common import AppiumOptions

from utils.constants import APPIUM_SERVER_URL, CAPABILITIES


@pytest.fixture(scope="session")
def driver():
    appium_driver_options = AppiumOptions().load_capabilities(CAPABILITIES)

    driver = webdriver.Remote(
        APPIUM_SERVER_URL,
        options=appium_driver_options
    )

    yield driver
    driver.quit()