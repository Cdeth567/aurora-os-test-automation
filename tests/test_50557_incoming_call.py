import pytest

from pages.main_page import MainPage


@pytest.mark.smoke
@pytest.mark.case_50557
def test_50557_incoming_call_creation(driver):
    main_page = MainPage(driver)

    main_page.wait_until_loaded()
    main_page.tap_incoming_call()
    main_page.wait_incoming_countdown_started()

    assert main_page.is_outgoing_button_disabled(), "Кнопка 'Исходящий вызов' должна стать disabled"
    assert main_page.is_incoming_button_disabled(), "Кнопка 'Входящий вызов' должна стать disabled"
    assert main_page.is_holding_disabled(), "Переключатель 'Удержание' должен стать disabled"
    assert main_page.is_dtmf_disabled(), "Переключатель 'DTMF' должен стать disabled"