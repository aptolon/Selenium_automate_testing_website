import pytest
from core.driver_manager import DriverManager
from pages.login_page import LoginPage
from utils.test_data import log_valid_user, log_invalid_user


@pytest.fixture
def setup():
    driver = DriverManager.get_driver()
    driver.get("https://arnypraht.com/login/")
    yield driver
    driver.quit()

# def test_valid_login(setup):
#     """Позитивный тест: Регистрация с валидными данными."""
#     page = LoginPage(setup)
#     page.login(
#         log_valid_user["email"], 
#         log_valid_user["password"], 
#     )
    
#     success_message = page.get_success_message()
#     assert "Мой аккаунт" in success_message, "Успешное сообщение о регистрации не найдено."


# def test_invalid_login(setup):
    
#     page = LoginPage(setup)
#     page.login(
#         log_invalid_user["email"], 
#         log_invalid_user["password"], 
#     )
#     error_message = page.get_error_message()
#     assert "Указанный пользователь не найден" in error_message, "Сообщение не найдено."
