from selenium.webdriver.common.by import By


class OrderPageLocators:
    name = (By.XPATH, '//input[@placeholder="* Имя"]')
    lastname = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    address = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    metro = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    select_item_in_dropdown_metro = (By.XPATH, '//li[@class="select-search__row"]')
    phone = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    date = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    button_next = (By.XPATH, '//button[text()="Далее"]')
    rental_period_field = (By.XPATH, '//div[text()="* Срок аренды"]')
    rental_period_dropdown_item = (By.XPATH, '//div[@class="Dropdown-menu"]/div[text()="трое суток"]')
    checkbox_gray_scooter = (By.XPATH, '//input[@id="grey"]')
    comment = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    button_make_order = (By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[text()="Заказать"]')
    button_yes_confirm_order = (By.XPATH, '//button[text()="Да"]')
    order_created_text = (By.XPATH, '//div[text()="Заказ оформлен"]')
