import pytest
from core.driver_manager import DriverManager
from pages.filters_page import FiltersPage
from time import sleep

@pytest.fixture
def setup():
    driver = DriverManager.get_driver()
    driver.get("https://arnypraht.com/shop/")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_filter_by_instock(setup):

    """Тест: Фильтрация по цвету."""
    page = FiltersPage(setup)
    total_items = page.get_total_items()
    page.select_instock_filter()
    sleep(2)
    filtered_items = page.get_total_items()
    assert filtered_items < total_items, "Фильтрация по наличию не работает."




def test_color_filter(setup):

    page = FiltersPage(setup)

    page.open_filters_bar()

    page.select_filter_option_by_index(2)
    sleep(2)

    displayed_colors = page.get_all_displayed_colors()
    assert all(color in ['Розово-красный', 'красный'] for color in displayed_colors), \
        f"Некорректный цвет товаров: {displayed_colors}"
    
    


# def test_no_items_with_invalid_color(setup):
#     page = FiltersPage(setup)

#     page.open_filters_bar()

#     page.select_instock_filter()
#     page.select_filter_option_by_index(11)

#     displayed_colors = page.get_all_displayed_colors()
#     assert len(displayed_colors) == 0, \
#         f"Ожидалось, что не будет отображаться ни одного цвета, но отображается: {displayed_colors}"



# # def test_reset_filters(setup):
# #     """Тест: Сброс фильтров."""
# #     page = FiltersPage(setup)
# #     total_items1 = page.get_total_items()
# #     page.select_instock_filter()
# #     sleep(2)
# #     filtered_items = page.get_total_items()
# #     page.reset_filters()
# #     sleep(2)
# #     total_items2 = page.get_total_items()
# #     assert total_items1 == total_items2, "total_items1 и total_items2 не равны"
# #     assert filtered_items < total_items1, "сброс не работает."