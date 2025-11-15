from selenium.webdriver.common.by import By


class MainPageLocators:
    order_button_in_header = (By.XPATH, '//button[@class="Button_Button__ra12g"]')
    order_button_in_page = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    faq_section = (By.XPATH, '//div[@class="Home_FAQ__3uVm4"]')

    @staticmethod
    def faq_question(id_number):
        return By.XPATH, f'//div[@id="accordion__heading-{id_number}"]'

    @staticmethod
    def faq_answer(id_number):
        return By.XPATH, f'//div[@id="accordion__panel-{id_number}"]'
