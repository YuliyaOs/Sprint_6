from pages.order_page import OrderPage
import pytest
import allure
import test_data
import configuration
from locators import base_page_locators


class TestOrder:

    @allure.title('Проверка кнопки «Заказать» вверху страницы')
    def test_order_button_in_head(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_site()
        order_page.click_order_button_in_head()

        assert driver.current_url == configuration.URL+configuration.order

    @allure.title('Проверка кнопки «Заказать» внизу страницы')
    def test_order_button_in_middle_page(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_site()
        order_page.click_order_button_in_middle_page()

        assert driver.current_url == configuration.URL+configuration.order

    @allure.title('Проверка заказа самоката')
    @pytest.mark.parametrize('name, surname, address, metro_station, phone, date, comment', [test_data.test_data_1, test_data.test_data_2])
    def test_order(self, driver, name, surname, address, metro_station, phone, date, comment):
        order_page = OrderPage(driver)
        order_page.go_to_site()
        order_page.click_order_button_in_head()
        order_page.input_order_form_1_part(
            name, surname, address, metro_station, phone)
        order_page.input_order_form_2_part(date, comment)
        order_number = order_page.get_order_number()

        assert order_number.is_displayed()

    @allure.title('Проверка перехода на главную страницу «Самоката» при клике на логотип «Самоката»')
    def test_scooter_button(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_site()
        order_page.click_order_button_in_head()
        order_page.click_to_element(base_page_locators.scooter_logo)

        assert driver.current_url == configuration.URL

    @allure.title('Проверка перехода на главную страницу Дзена при клике на логотип Яндекса')
    def test_yandex_button(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_site()
        order_page.click_yandex_logo()

        assert driver.current_url == configuration.url_dzen
