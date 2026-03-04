from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from locators import order_page_locators
import pages.base_page as base_page


class OrderPage(base_page.BasePage):

    def click_order_button_in_middle_page(self):
        wait = WebDriverWait(self.driver, 3)
        self.driver.find_element(
            *order_page_locators.order_form_button_middle_page).click()
        wait.until(expected_conditions.presence_of_element_located(
            order_page_locators.for_whom_scooter_header))

    def input_order_form_1_part(self, name, surname, address, metro_station, phone):
        wait = WebDriverWait(self.driver, 3)
        self.driver.find_element(
            *order_page_locators.name_input).send_keys(name)
        self.driver.find_element(
            *order_page_locators.surname_input).send_keys(surname)
        self.driver.find_element(
            *order_page_locators.address_input).send_keys(address)
        self.driver.find_element(
            *order_page_locators.metro_station_input).click()
        self.driver.find_element(
            *order_page_locators.metro_station_input).send_keys(metro_station)
        self.driver.find_element(
            *order_page_locators.metro_station_input).send_keys(Keys.DOWN)
        self.driver.find_element(
            *order_page_locators.metro_station_input).send_keys(Keys.ENTER)
        self.driver.find_element(
            *order_page_locators.phone_input).send_keys(phone)
        self.driver.find_element(*order_page_locators.next_button).click()
        wait.until(expected_conditions.visibility_of_element_located(
            order_page_locators.about_renting_header))

    def input_order_form_2_part(self, date, comment):
        wait = WebDriverWait(self.driver, 3)
        self.driver.find_element(
            *order_page_locators.when_input).send_keys(date)
        self.driver.find_element(
            *order_page_locators.when_input).send_keys(Keys.ENTER)
        self.driver.find_element(
            *order_page_locators.rental_period_open).click()
        wait.until(expected_conditions.visibility_of_element_located(
            order_page_locators.rental_period_day))
        self.driver.find_element(
            *order_page_locators.rental_period_day).click()
        self.driver.find_element(
            *order_page_locators.color_scooter_black).click()
        self.driver.find_element(
            *order_page_locators.comment_input).send_keys(comment)
        self.driver.find_element(*order_page_locators.order_button).click()
        wait.until(expected_conditions.visibility_of_element_located(
            order_page_locators.order_modal_header))
        self.driver.find_element(*order_page_locators.yes_button).click()
        wait.until(expected_conditions.visibility_of_element_located(
            order_page_locators.order_number))

    def get_message_about_order(self):
        order_number = self.driver.find_element(
            *order_page_locators.order_number)
        view_status_button = self.driver.find_element(
            *order_page_locators.view_status_button)
        return order_number, view_status_button
