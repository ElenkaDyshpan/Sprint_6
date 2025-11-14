import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    @allure.step('Кликнуть по кнопке "Заказать"')
    def click_order_button(self, order_button_locator):
        self.scroll_to_element(order_button_locator)
        self.wait_visibility_of_element(order_button_locator)
        self.click_on_element(order_button_locator)

    @allure.step('Получить текст ответа на вопрос из блока "Вопросы о важном"')
    def get_faq_question_answer_text(self, data):
        self.scroll_to_element(MainPageLocators.faq_section)
        self.wait_visibility_of_element(MainPageLocators.faq_section)
        self.click_on_element(MainPageLocators.faq_question(data))
        self.wait_visibility_of_element(MainPageLocators.faq_answer(data))
        return self.get_text_on_element(MainPageLocators.faq_answer(data))
