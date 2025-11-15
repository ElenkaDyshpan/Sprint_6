import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step('Заполнение первой части формы и нажатие кнопки "Далее"')
    def data_entry_first_form(self, test_data):
        self.wait_visibility_of_element(OrderPageLocators.name)
        self.click_on_element(OrderPageLocators.name)
        self.set_keys_to_input(OrderPageLocators.name, test_data['name'])
        self.click_on_element(OrderPageLocators.lastname)
        self.set_keys_to_input(OrderPageLocators.lastname, test_data['lastname'])
        self.click_on_element(OrderPageLocators.address)
        self.set_keys_to_input(OrderPageLocators.address, test_data['address'])
        self.click_on_element(OrderPageLocators.metro)
        self.set_keys_to_input(OrderPageLocators.metro, test_data['metro'])
        self.click_on_element(OrderPageLocators.select_item_in_dropdown_metro)
        self.click_on_element(OrderPageLocators.phone)
        self.set_keys_to_input(OrderPageLocators.phone, test_data['phone'])
        self.click_on_element(OrderPageLocators.button_next)

    @allure.step('Заполнение второй части формы и окно подтверждения')
    def data_entry_second_form(self, test_data):
        self.wait_visibility_of_element(OrderPageLocators.date)
        self.click_on_element(OrderPageLocators.date)
        self.set_keys_to_input(OrderPageLocators.date, test_data['date'])
        self.click_on_element(OrderPageLocators.checkbox_gray_scooter)
        self.click_on_element(OrderPageLocators.rental_period_field)
        self.click_on_element(OrderPageLocators.rental_period_dropdown_item)
        self.click_on_element(OrderPageLocators.comment)
        self.set_keys_to_input(OrderPageLocators.comment, test_data['comment'])
        self.click_on_element(OrderPageLocators.button_make_order)
        self.wait_visibility_of_element(OrderPageLocators.button_yes_confirm_order)
        self.click_on_element(OrderPageLocators.button_yes_confirm_order)

    @allure.step('Проверка отображения текста "Заказ оформлен" после создания заказа')
    def check_order_created_text_visibility(self):
        return self.check_displaying_of_element(OrderPageLocators.order_created_text)
