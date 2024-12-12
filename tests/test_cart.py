import pytest
from core.driver_manager import DriverManager
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from utils.test_data import cart_invalid_promo, log_valid_user

import time


@pytest.fixture
def setup():
    driver = DriverManager.get_driver()
    driver.get("https://arnypraht.com/shop/")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_add_item_to_cart(setup):
    """Тест: Добавление товара в корзину."""
    page = CartPage(setup)
    page.add_item_to_cart()
    page.navigate_to_cart()
    assert not page.is_cart_empty(), "Корзина пуста после добавления товара."

def test_edit_item_quantity_in_cart(setup):
    """Тест: Редактирование количества товаров в корзине."""
    page = CartPage(setup)
    page.add_item_to_cart()
    page.navigate_to_cart()
    initial_price = page.get_total_price()
    page.change_item_quantity(2)
    time.sleep(2)
    
    updated_price = page.get_total_price()
    assert updated_price != initial_price, "Цена не обновилась после изменения количества."

def test_remove_item_from_cart(setup):
    """Тест: Удаление товара из корзины."""
    page = CartPage(setup)
    page.add_item_to_cart()
    page.navigate_to_cart()
    page.remove_item_from_cart()
    time.sleep(2)
    assert page.is_cart_empty(), "Корзина не пуста после удаления товара."
    
    
def test_invalid_promocode(setup):
    """Негативный тест: ввод невалидного промокода."""
    page = LoginPage(setup)
    setup.get("https://arnypraht.com/login")
    page.login(
         log_valid_user["email"], 
         log_valid_user["password"], 
     )
    page = CartPage(setup)
    setup.get("https://arnypraht.com/shop/")
    page.add_item_to_cart()
    page.navigate_to_cart()
    page.enter_promocode(cart_invalid_promo)
    error_message = page.get_error_message()
    assert "Промокод не найден!" in error_message, "Сообщение не найдено."

