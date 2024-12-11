import pytest
from core.driver_manager import DriverManager
from pages.navigation_page import NavigationPage

@pytest.fixture
def setup():
    driver = DriverManager.get_driver()
    driver.get("https://arnypraht.com")
    yield driver
    driver.quit()

# def test_navigation_to_bags(setup):
#     """Тест: Переход на страницу 'Сумки'."""
#     page = NavigationPage(setup)
#     page.navigate_to_bags()
#     assert "/category/bags/" in setup.current_url, "Не удалось перейти на страницу 'Сумки'."

# def test_navigation_to_contacts(setup):
#     """Тест: Переход на страницу 'Контакты'."""
#     page = NavigationPage(setup)
#     page.navigate_to_contacts()
#     assert "/contact-us/" in setup.current_url, "Не удалось перейти на страницу 'Контакты'."

# def test_navigation_to_find_store(setup):
#     """Тест: Переход на страницу 'Найти магазин'."""
#     page = NavigationPage(setup)
#     page.navigate_to_find_store()
#     assert "/shops/" in setup.current_url, "Не удалось перейти на страницу 'Найти магазин'."


# def test_navigation_to_jewelry(setup):
#     """Тест: Переход на страницу 'Украшения ARNY'."""
#     page = NavigationPage(setup)
#     page.navigate_to_jewelry()
#     assert "/category/aksessuary/ukrasheniya-arny/" in setup.current_url, "Не удалось перейти на страницу 'Украшения ARNY'."
