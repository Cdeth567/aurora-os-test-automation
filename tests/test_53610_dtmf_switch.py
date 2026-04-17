import pytest

from pages.main_page import MainPage


@pytest.mark.case_53610
def test_53610_dtmf_switch_can_be_enabled(driver):
    page = MainPage(driver)

    page.wait_until_loaded()
    page.enable_dtmf()

    assert page.is_dtmf_placeholder_visible(), (
        "После включения DTMF должен отображаться текст 'Текст DTMF'"
    )