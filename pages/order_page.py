from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class OrderPage:

    order_form_button_in_head = [By.XPATH, "(.//button[text()='Заказать'])[1]"]
    order_form_button_middle_page = [
        By.XPATH, "(.//button[text()='Заказать'])[2]"]
    for_whom_scooter_header = [By.XPATH, ".//div[text()='Для кого самокат']"]
    name_input = [By.XPATH, ".//input[contains(@placeholder, 'Имя')]"]
    surname_input = [By.XPATH, ".//input[contains(@placeholder, 'Фамилия')]"]
    address_input = [By.XPATH, ".//input[contains(@placeholder, 'Адрес')]"]
    metro_station_input = [
        By.XPATH, ".//input[contains(@placeholder, 'Станция')]"]
    phone_input = [By.XPATH, ".//input[contains(@placeholder, 'Телефон')]"]
    next_button = [By.XPATH, ".//button[text()='Далее']"]
    about_renting_header = [By.XPATH, ".//div[text()='Про аренду']"]
    when_input = [By.XPATH, ".//input[contains(@placeholder, 'Когда')]"]
    rental_period_open = [By.XPATH, ".//div[contains(text(), 'Срок')]"]
    rental_period_day = [By.XPATH, ".//div[contains(text(), 'сутки')]"]
    color_scooter_black = [By.XPATH, ".//label/input[@id='black']"]
    comment_input = [
        By.XPATH, ".//input[contains(@placeholder, 'Комментарий')]"]
    order_button = [By.XPATH, "(.//button[text()='Заказать'])[2]"]
    order_modal_header = [By.XPATH, ".//div[text()='Хотите оформить заказ?']"]
    yes_button = [By.XPATH, ".//button[text()='Да']"]
    order_placed = [By.XPATH, ".//div[text()='Заказ оформлен']"]
    yandex_logo = [By.XPATH, ".//img[@alt='Yandex']"]
    scooter_logo = [By.XPATH, ".//img[@alt='Scooter']"]
    rcc_confirm_button = [By.XPATH, ".//button[@id='rcc-confirm-button']"]

    def __init__(self, driver):
        self.driver = driver

    def click_order_button_in_head(self):
        wait = WebDriverWait(self.driver, 3)
        self.driver.find_element(*self.order_form_button_in_head).click()
        wait.until(expected_conditions.presence_of_element_located(
            self.for_whom_scooter_header))

    def click_order_button_in_middle_page(self):
        wait = WebDriverWait(self.driver, 3)
        self.driver.find_element(*self.order_form_button_middle_page).click()
        wait.until(expected_conditions.presence_of_element_located(
            self.for_whom_scooter_header))

    def input_order_form_1_part(self, name, surname, address, metro_station, phone):
        wait = WebDriverWait(self.driver, 3)
        self.driver.find_element(*self.name_input).send_keys(name)
        self.driver.find_element(*self.surname_input).send_keys(surname)
        self.driver.find_element(*self.address_input).send_keys(address)
        self.driver.find_element(
            *self.metro_station_input).click()
        self.driver.find_element(
            *self.metro_station_input).send_keys(metro_station)
        self.driver.find_element(
            *self.metro_station_input).send_keys(Keys.DOWN)
        self.driver.find_element(
            *self.metro_station_input).send_keys(Keys.ENTER)
        self.driver.find_element(*self.phone_input).send_keys(phone)
        self.driver.find_element(*self.next_button).click()
        wait.until(expected_conditions.visibility_of_element_located(
            self.about_renting_header))

    def input_order_form_2_part(self, date, comment):
        wait = WebDriverWait(self.driver, 3)
        self.driver.find_element(*self.when_input).send_keys(date)
        self.driver.find_element(*self.when_input).send_keys(Keys.ENTER)
        self.driver.find_element(*self.rental_period_open).click()
        wait.until(expected_conditions.visibility_of_element_located(
            self.rental_period_day))
        self.driver.find_element(*self.rental_period_day).click()
        self.driver.find_element(*self.color_scooter_black).click()
        self.driver.find_element(*self.comment_input).send_keys(comment)
        self.driver.find_element(*self.order_button).click()
        wait.until(expected_conditions.visibility_of_element_located(
            self.order_modal_header))
        self.driver.find_element(*self.yes_button).click()
        wait.until(expected_conditions.visibility_of_element_located(
            self.order_placed))

    def click_scooter_logo(self):
        self.driver.find_element(*self.scooter_logo).click()
        return self.driver.current_url

    def click_yandex_logo(self):
        wait = WebDriverWait(self.driver, 10)
        original_window = self.driver.current_window_handle
        assert len(self.driver.window_handles) == 1
        self.driver.find_element(*self.yandex_logo).click()
        wait.until(expected_conditions.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        wait.until(expected_conditions.title_is(
            "Дзен — главная новостная информационная платформа, которая помогает миллионам людей узнавать, что происходит в мире."))
        return self.driver.current_url

    def get_message_about_order(self):
        return self.driver.find_element(*self.order_placed)
