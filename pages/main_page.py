from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def wait_until_loaded(self) -> None:
        self.wait_visible(MainPageLocators.MAIN_PAGE, timeout=10)
        self.wait_visible(MainPageLocators.TITLE, timeout=10)
        self.wait_visible(MainPageLocators.OUTGOING_CALL_BUTTON, timeout=10)
        self.wait_visible(MainPageLocators.INCOMING_CALL_BUTTON, timeout=10)

    def has_loader(self) -> bool:
        return self.is_visible(MainPageLocators.SPINNER, timeout=5)

    def tap_outgoing_call(self) -> None:
        self.click(MainPageLocators.OUTGOING_CALL_BUTTON, timeout=10)

    def tap_incoming_call(self) -> None:
        self.click(MainPageLocators.INCOMING_CALL_BUTTON, timeout=10)