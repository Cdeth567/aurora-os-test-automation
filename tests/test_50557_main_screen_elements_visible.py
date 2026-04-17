import pytest

from pages.main_page import MainPage


@pytest.mark.smoke
@pytest.mark.case_50557
def test_50557_main_screen_elements_visible(driver):
    page = MainPage(driver)

    page.wait_until_loaded()
    assert page.are_main_controls_visible(), (
        "На главной странице должны отображаться разделы 'Звонки' и 'Функции', "
        "кнопки 'Исходящий вызов'/'Входящий вызов' и переключатели 'Удержание'/'DTMF'"
    )