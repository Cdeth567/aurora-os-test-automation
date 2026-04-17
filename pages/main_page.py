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

    def wait_incoming_countdown_started(self) -> None:
        self.wait_visible(MainPageLocators.INCOMING_COUNTDOWN, timeout=5)

    def are_main_controls_visible(self) -> bool:
        locators = [
            MainPageLocators.MAIN_PAGE,
            MainPageLocators.CALLS,
            MainPageLocators.OUTGOING_CALL_BUTTON,
            MainPageLocators.INCOMING_CALL_BUTTON,
            MainPageLocators.FUNCTIONS,
            MainPageLocators.HOLDING_SWITCH,
            MainPageLocators.DTMF_SWITCH,
        ]
        return all(self.is_visible(locator, timeout=3) for locator in locators)

    def is_outgoing_button_disabled(self) -> bool:
        return self.get_attribute(MainPageLocators.OUTGOING_CALL_BUTTON, "enabled", timeout=5) == "false"

    def is_incoming_button_disabled(self) -> bool:
        return self.get_attribute(MainPageLocators.INCOMING_CALL_BUTTON, "enabled", timeout=5) == "false"

    def is_holding_disabled(self) -> bool:
        return self.get_attribute(MainPageLocators.HOLDING_SWITCH, "enabled", timeout=5) == "false"

    def is_dtmf_disabled(self) -> bool:
        return self.get_attribute(MainPageLocators.DTMF_SWITCH, "enabled", timeout=5) == "false"

    def _click_until(self, click_targets, condition, timeout_after_click: int = 2) -> bool:
        for locator in click_targets:
            try:
                self.click(locator, timeout=5)
            except Exception:
                continue

            if self.wait_until(condition, timeout=timeout_after_click):
                return True

        return False

    def enable_holding(self) -> None:
        if self.is_holding_enabled():
            return

        self._click_until(
            [
                MainPageLocators.HOLDING_DESCRIPTION,
                MainPageLocators.HOLDING_TITLE,
                MainPageLocators.HOLDING_SWITCH,
            ],
            self.is_holding_enabled,
            timeout_after_click=3,
        )

    def is_holding_enabled(self) -> bool:
        return self.get_attribute(MainPageLocators.HOLDING_SWITCH, "checked", timeout=5) == "true"

    def enable_dtmf(self) -> None:
        if self.is_dtmf_enabled() or self.is_dtmf_placeholder_visible():
            return

        self._click_until(
            [
                MainPageLocators.DTMF_DESCRIPTION,
                MainPageLocators.DTMF_TITLE,
                MainPageLocators.DTMF_SWITCH,
            ],
            lambda: self.is_dtmf_enabled() or self.is_dtmf_placeholder_visible(),
            timeout_after_click=3,
        )

    def is_dtmf_enabled(self) -> bool:
        return self.get_attribute(MainPageLocators.DTMF_SWITCH, "checked", timeout=5) == "true"

    def is_dtmf_placeholder_visible(self) -> bool:
        return self.is_visible(MainPageLocators.DTMF_PLACEHOLDER, timeout=5)
