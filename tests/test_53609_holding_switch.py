import pytest

from pages.main_page import MainPage


@pytest.mark.case_53609
def test_53609_holding_switch_can_be_enabled(driver):
    page = MainPage(driver)

    page.wait_until_loaded()
    page.enable_holding()

    assert page.is_holding_enabled(), "Переключатель 'Удержание' должен перейти во включенное состояние"
