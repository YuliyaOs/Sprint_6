from selenium.webdriver.common.keys import Keys
from locators import order_page_locators
from pages.base_page import BasePage


class OrderPage(BasePage):

    def click_order_button_in_middle_page(self):
        self.click_to_element(
            order_page_locators.order_form_button_middle_page)
        self.wait_visibility_of_element(
            order_page_locators.for_whom_scooter_header)

    def input_order_form_1_part(self, name, surname, address, metro_station, phone):
        self.enter_data_in_field(order_page_locators.name_input, name)
        self.enter_data_in_field(order_page_locators.surname_input, surname)
        self.enter_data_in_field(order_page_locators.address_input, address)
        self.click_to_element(order_page_locators.metro_station_input)
        self.enter_data_in_field(
            order_page_locators.metro_station_input, metro_station)
        self.enter_data_in_field(
            order_page_locators.metro_station_input, Keys.DOWN)
        self.enter_data_in_field(
            order_page_locators.metro_station_input, Keys.ENTER)
        self.enter_data_in_field(order_page_locators.phone_input, phone)
        self.click_to_element(order_page_locators.next_button)
        self.wait_visibility_of_element(
            order_page_locators.about_renting_header)

    def input_order_form_2_part(self, date, comment):
        self.enter_data_in_field(order_page_locators.when_input, date)
        self.enter_data_in_field(order_page_locators.when_input, Keys.ENTER)
        self.click_to_element(order_page_locators.rental_period_open)
        self.wait_visibility_of_element(order_page_locators.rental_period_day)
        self.click_to_element(order_page_locators.rental_period_day)
        self.click_to_element(order_page_locators.color_scooter_black)
        self.enter_data_in_field(order_page_locators.comment_input, comment)
        self.click_to_element(order_page_locators.order_button)
        self.wait_visibility_of_element(order_page_locators.order_modal_header)
        self.click_to_element(order_page_locators.yes_button)
        self.wait_visibility_of_element(order_page_locators.order_number)

    def get_order_number(self):
        order_number = self.find_element(
            order_page_locators.order_number)
        return order_number
