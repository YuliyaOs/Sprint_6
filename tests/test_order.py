from selenium import webdriver
from pages.order_page import OrderPage
import pytest
import allure
import test_data
import configuration
from locators import order_page_locators


class TestOrder:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(configuration.URL)
        cls.driver.find_element(
            *order_page_locators.rcc_confirm_button).click()

    @allure.title('Проверка кнопки «Заказать» вверху страницы')
    def test_order_button_in_head(self):
        order_page = OrderPage(self.driver)
        order_page.click_order_button_in_head()
        assert self.driver.current_url == configuration.URL+configuration.order

    @allure.title('Проверка кнопки «Заказать» внизу страницы')
    def test_order_button_in_middle_page(self):
        order_page = OrderPage(self.driver)
        order_page.go_to_main_page()
        order_page.click_order_button_in_middle_page()
        assert self.driver.current_url == configuration.URL+configuration.order

    @allure.title('Проверка заказа самоката')
    @pytest.mark.parametrize('name, surname, address, metro_station, phone, date, comment', [test_data.test_data_1, test_data.test_data_2])
    def test_order(self, name, surname, address, metro_station, phone, date, comment):
        order_page = OrderPage(self.driver)
        order_page.go_to_main_page()
        order_page.click_order_button_in_head()
        order_page.input_order_form_1_part(
            name, surname, address, metro_station, phone)
        order_page.input_order_form_2_part(date, comment)
        order_number, view_status_button = order_page.get_message_about_order()
        assert order_number.is_displayed() and view_status_button.is_displayed()

    @allure.title('Проверка перехода на главную страницу «Самоката» при клике на логотип «Самоката»')
    def test_scooter_button(self):
        order_page = OrderPage(self.driver)
        order_page.go_to_main_page()
        order_page.click_order_button_in_head()
        url = order_page.click_scooter_logo()
        assert url == configuration.URL

    @allure.title('Проверка перехода на главную страницу Дзена при клике на логотип Яндекса')
    def test_yandex_button(self):
        order_page = OrderPage(self.driver)
        order_page.go_to_main_page()
        url = order_page.click_yandex_logo()
        assert url == configuration.url_dzen

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
