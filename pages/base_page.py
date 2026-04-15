from __future__ import annotations

from typing import Tuple

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait


Locator = Tuple[str, str]


class BasePage:
    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.timeout = timeout

    def _first_visible(self, locator: Locator):
        by, value = locator
        elements = self.driver.find_elements(by, value)

        for element in elements:
            try:
                if element.is_displayed():
                    return element
            except Exception:
                continue

        return False

    def wait_visible(self, locator: Locator, timeout: int | None = None) -> WebElement:
        actual_timeout = timeout or self.timeout
        wait = WebDriverWait(self.driver, actual_timeout)
        return wait.until(lambda d: self._first_visible(locator))

    def wait_visible_optional(self, locator: Locator, timeout: int | None = None) -> bool:
        actual_timeout = timeout or self.timeout
        wait = WebDriverWait(self.driver, actual_timeout)

        try:
            wait.until(lambda d: self._first_visible(locator))
            return True
        except Exception:
            return False

    def click(self, locator: Locator, timeout: int | None = None) -> None:
        element = self.wait_visible(locator, timeout)
        element.click()

    def is_visible(self, locator: Locator, timeout: int | None = None) -> bool:
        return self.wait_visible_optional(locator, timeout)

    def get_element(self, locator: Locator, timeout: int | None = None) -> WebElement:
        return self.wait_visible(locator, timeout)

    def save_debug_artifacts(self, prefix: str = "debug") -> None:
        with open(f"{prefix}.xml", "w", encoding="utf-8") as file:
            file.write(self.driver.page_source)

        self.driver.save_screenshot(f"{prefix}.png")