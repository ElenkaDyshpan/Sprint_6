from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure
from locators.base_page_locators import BasePageLocators


# from locators.main_page_locators import MainPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('Подождать прогрузки элемента')
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Кликнуть на элемент')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Ввести значение в поле в ввода')
    def set_keys_to_input(self, locator, keys):
        self.driver.find_element(*locator).send_keys(keys)

    @allure.step('Получить текст на элементе')
    def get_text_on_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Перейти на другую вкладку')
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Проверить отображение элемента')
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Получить текущий url')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Дождаться перехода на страницу')
    def wait_load_url(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))

    @allure.step('Кликнуть по надписи "Самокат" в хедере')
    def click_on_header_logo_scooter(self):
        self.wait_visibility_of_element(BasePageLocators.header_logo_scooter)
        self.click_on_element(BasePageLocators.header_logo_scooter)

    @allure.step('Кликнуть по надписи "Яндекс" в хедере')
    def click_on_header_logo_yandex(self):
        self.wait_visibility_of_element(BasePageLocators.header_logo_yandex)
        self.click_on_element(BasePageLocators.header_logo_yandex)