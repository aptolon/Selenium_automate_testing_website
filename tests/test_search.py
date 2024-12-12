import pytest
from selenium import webdriver
from pages.search_page import SearchPage
from utils.test_data import search_valid_query, search_invalid_query, search_partial_query

@pytest.fixture
def driver():
    """Фикстура для инициализации и завершения WebDriver."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://arnypraht.com/")  # Замените на URL целевого сайта
    yield driver
    driver.quit()

def test_search_valid_query(driver):
    """Позитивный тест: проверка поиска с корректным запросом."""
    search_page = SearchPage(driver)
    search_page.enter_search_query(search_valid_query["query"])  # Пример запроса
    search_page.submit_search()
    assert search_page.get_search_results(), "Результаты поиска отсутствуют!"
# py -m pytest tests/test_search.py::test_search_valid_query --html=reports/report.html

def test_search_no_results(driver):
    """Негативный тест: проверка поиска с некорректным запросом."""
    search_page = SearchPage(driver)
    search_page.enter_search_query(search_invalid_query["query"])  # Пример запроса, не дающего результатов
    search_page.submit_search()
    results = search_page.get_search_results()
    assert len(results) == 0, "Результаты поиска должны отсутствовать!"

def test_search_partial_match(driver):
    """Тест: проверка поиска по частичному совпадению."""
    search_page = SearchPage(driver)
    search_page.enter_search_query(search_partial_query["part_query"])
    search_page.submit_search()
    assert search_page.is_search_result_present(search_partial_query["query"]), "Частичное совпадение не найдено!"
