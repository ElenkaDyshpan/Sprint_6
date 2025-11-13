from selenium.webdriver.common.by import By


class BasePageLocators:
    header_logo_scooter = (By.XPATH, '//a[@href="/"]')
    header_logo_yandex = (By.XPATH, '//a[@href="//yandex.ru"]')
