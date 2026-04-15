from locators.call_page_locators import CallPageLocators
from pages.base_page import BasePage


class CallPage(BasePage):
    def wait_until_outgoing_call_screen_opened(self) -> None:
        self.wait_visible(CallPageLocators.REMOTE_NAME_TEXT, timeout=10)
        self.wait_visible(CallPageLocators.CONNECTION_TEXT, timeout=10)

    def is_connection_visible(self) -> bool:
        return self.is_visible(CallPageLocators.CONNECTION_TEXT, timeout=5)

    def is_remote_name_visible(self) -> bool:
        return self.is_visible(CallPageLocators.REMOTE_NAME_TEXT, timeout=5)

    def connection_below_remote_name(self) -> bool:
        connection = self.get_element(CallPageLocators.CONNECTION_TEXT, timeout=5)
        remote_name = self.get_element(CallPageLocators.REMOTE_NAME_TEXT, timeout=5)
        return connection.location["y"] > remote_name.location["y"]