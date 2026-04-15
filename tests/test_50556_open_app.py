import pytest

from pages.main_page import MainPage


@pytest.mark.smoke
@pytest.mark.case_50556
def test_50556_open_app(driver):
    main_page = MainPage(driver)

    spinner_found = main_page.has_loader()
    print(f"spinner found: {spinner_found}")
    assert spinner_found, "Во время открытия приложения не найден индикатор загрузки"

    main_page.wait_until_loaded()