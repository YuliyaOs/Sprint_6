from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import order_page_locators
from locators import base_page_locators
import configuration


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator))

    def enter_data_in_field(self, locator, data):
        self.find_element(locator).send_keys(data)

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_element_to_clickable(self, locator, time=10):
        WebDriverWait(self.driver, time).until(
            expected_conditions.element_to_be_clickable(locator))

    def wait_visibility_of_element(self, locator, time=10):
        WebDriverWait(self.driver, time).until(
            expected_conditions.visibility_of_element_located(locator))

    def wait_presence_of_element(self, locator, time=10):
        WebDriverWait(self.driver, time).until(
            expected_conditions.presence_of_element_located(locator))

    def click_to_element(self, locator):
        self.find_element(locator).click()

    def click_yandex_logo(self):
        wait = WebDriverWait(self.driver, 10)
        original_window = self.driver.current_window_handle
        self.click_to_element(base_page_locators.yandex_logo)
        wait.until(expected_conditions.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        wait.until(expected_conditions.title_is(
            base_page_locators.title_page_dzen))

    def click_order_button_in_head(self):
        self.click_to_element(
            base_page_locators.order_form_button_in_head)
        self.wait_presence_of_element(
            order_page_locators.for_whom_scooter_header)

    def go_to_site(self):
        self.driver.get(configuration.URL)

    def get_current_url(self):
        return self.driver.current_url
