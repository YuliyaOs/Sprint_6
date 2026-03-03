from selenium import webdriver
from pages.order_page import OrderPage
import pytest
import allure
import test_data
import configuration
from pages.order_page import OrderPage


class TestOrder:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(configuration.URL)
        cls.driver.find_element(*OrderPage.rcc_confirm_button).click()

    @allure.title('Проверка кнопки «Заказать» вверху страницы')
    def test_order_button_in_head(self):
        order_page = OrderPage(self.driver)
        order_page.click_order_button_in_head()
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/order'
        self.driver.get(configuration.URL)

    @allure.title('Проверка кнопки «Заказать» внизу страницы')
    def test_order_button_in_middle_page(self):
        order_page = OrderPage(self.driver)
        order_page.click_order_button_in_middle_page()
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/order'
        self.driver.get(configuration.URL)

    @allure.title('Проверка заказа самоката')
    @pytest.mark.parametrize('name, surname, address, metro_station, phone, date, comment', [test_data.test_data_1, test_data.test_data_2])
    def test_order(self, name, surname, address, metro_station, phone, date, comment):
        order_page = OrderPage(self.driver)
        order_page.click_order_button_in_head()
        order_page.input_order_form_1_part(
            name, surname, address, metro_station, phone)
        order_page.input_order_form_2_part(date, comment)
        assert 'Заказ оформлен' in order_page.get_message_about_order().text
        self.driver.get(configuration.URL)

    @allure.title('Проверка перехода на главную страницу «Самоката» при клике на логотип «Самоката»')
    def test_scooter_button(self):
        order_page = OrderPage(self.driver)
        order_page.click_order_button_in_head()
        url = order_page.click_scooter_logo()
        assert url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.title('Проверка перехода на главную страницу Дзена при клике на логотип Яндекса')
    def test_yandex_button(self):
        order_page = OrderPage(self.driver)
        url = order_page.click_yandex_logo()
        assert url == 'https://dzen.ru/?yredirect=true'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
