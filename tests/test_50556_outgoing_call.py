import pytest
from selenium.common.exceptions import TimeoutException

from pages.main_page import MainPage
from pages.call_page import CallPage


@pytest.mark.smoke
@pytest.mark.case_50556
def test_50556_outgoing_call_creation(driver):
    main_page = MainPage(driver)
    call_page = CallPage(driver)

    main_page.wait_until_loaded()
    main_page.tap_outgoing_call()

    try:
        call_page.wait_until_outgoing_call_screen_opened()
    except TimeoutException:
        call_page.save_debug_artifacts(prefix="outgoing_call_not_opened")
        pytest.fail(
            "После нажатия на 'Исходящий вызов' экран звонка не открылся. "
            "Сохранены outgoing_call_not_opened.xml и outgoing_call_not_opened.png"
        )

    assert call_page.is_remote_name_visible(), "Не отображается 'Remote name'"
    assert call_page.is_connection_visible(), "Не отображается 'Соединение'"
    assert call_page.connection_below_remote_name(), (
        "'Соединение' должно быть расположено ниже 'Remote name'"
    )