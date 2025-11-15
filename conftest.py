import pytest
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver

from curl import *


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def start_from_main_page(driver: WebDriver):
    main_page = base_url
    driver.get(main_page)
    return driver


@pytest.fixture()
def start_from_order_page(driver: WebDriver):
    order_page = order_url
    driver.get(order_page)
    return driver
