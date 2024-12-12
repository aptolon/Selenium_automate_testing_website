import pytest
from core.driver_manager import DriverManager
from pages.registration_page import RegistrationPage
from utils.test_data import reg_valid_user, reg_invalid_user


@pytest.fixture
def setup():
    driver = DriverManager.get_driver()
    driver.get("https://arnypraht.com/register/")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_registration(setup):
    """Позитивный тест: Регистрация с валидными данными."""
    page = RegistrationPage(setup)
    page.register(
        reg_valid_user["email"], 
        reg_valid_user["mobile_phone"], 
        reg_valid_user["password"], 
        reg_valid_user["gender"], 
        reg_valid_user["dob"]
    )
    success_message = page.get_success_message()
    assert "Спасибо за регистрацию!" in success_message, "Успешное сообщение о регистрации не найдено."


def test_invalid_email(setup):
    """Негативный тест: Регистрация с невалидным email."""
    page = RegistrationPage(setup)
    page.register(
        reg_invalid_user["email"], 
        reg_invalid_user["mobile_phone"], 
        reg_invalid_user["password"], 
        reg_invalid_user["gender"], 
        reg_invalid_user["dob"]
    )
    error_message = page.get_error_message()
    assert "Не могу создать нового пользователя: Пользователь с таким номером телефона уже зарегистрирован!" in error_message, "Сообщение о некорректном телефоне не найдено."
