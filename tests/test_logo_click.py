import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from curl import base_url, zen_url


class TestLogoClick:
    @allure.title('Проверка перехода на главную страницу')
    @allure.description('Тестирование переходна на главную страницу сервиса при клике на надпись "Самокат" в логотипе')
    def test_move_to_main_page_by_scooter_logo_part(self, start_from_order_page):
        order_page = OrderPage(start_from_order_page)
        order_page.click_on_header_logo_scooter()
        assert order_page.get_current_url() == base_url

    @allure.title('Проверка перехода на страницу Дзена')
    @allure.description('Тестирование перехода на главную страницу Дзена при клике на надпись "Яндекс" в логотипе')
    def test_move_to_zen_page_by_yandex_logo_part(self, start_from_main_page):
        main_page = MainPage(start_from_main_page)
        main_page.click_on_header_logo_yandex()
        main_page.switch_to_next_tab()
        main_page.wait_load_url(zen_url)
        assert main_page.get_current_url() == zen_url
        