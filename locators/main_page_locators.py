from selenium.webdriver.common import by
from selenium.webdriver.common.by import By


class MainPageLocators:
    order_button_in_header = (By.XPATH, '//button[@class="Button_Button__ra12g"]')
    order_button_in_page = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    faq_section = (By.XPATH, '//div[@class="Home_FAQ__3uVm4"]')
    faq_questions = {
        1: (By.XPATH, '//div[@id="accordion__heading-0"]'),
        2: (By.XPATH, '//div[@id="accordion__heading-1"]'),
        3: (By.XPATH, '//div[@id="accordion__heading-2"]'),
        4: (By.XPATH, '//div[@id="accordion__heading-3"]'),
        5: (By.XPATH, '//div[@id="accordion__heading-4"]'),
        6: (By.XPATH, '//div[@id="accordion__heading-5"]'),
        7: (By.XPATH, '//div[@id="accordion__heading-6"]'),
        8: (By.XPATH, '//div[@id="accordion__heading-7"]')
    }
    faq_answers = {
        1: (By.XPATH, '//div[@id="accordion__panel-0"]'),
        2: (By.XPATH, '//div[@id="accordion__panel-1"]'),
        3: (By.XPATH, '//div[@id="accordion__panel-2"]'),
        4: (By.XPATH, '//div[@id="accordion__panel-3"]'),
        5: (By.XPATH, '//div[@id="accordion__panel-4"]'),
        6: (By.XPATH, '//div[@id="accordion__panel-5"]'),
        7: (By.XPATH, '//div[@id="accordion__panel-6"]'),
        8: (By.XPATH, '//div[@id="accordion__panel-7"]')
    }