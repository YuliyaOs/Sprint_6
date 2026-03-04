from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import order_page_locators
from locators import base_page_locators
import configuration


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_scooter_logo(self):
        self.driver.find_element(*base_page_locators.scooter_logo).click()
        return self.driver.current_url

    def click_yandex_logo(self):
        wait = WebDriverWait(self.driver, 10)
        original_window = self.driver.current_window_handle
        assert len(self.driver.window_handles) == 1
        self.driver.find_element(*base_page_locators.yandex_logo).click()
        wait.until(expected_conditions.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break
        wait.until(expected_conditions.title_is(
            base_page_locators.title_page_dzen))
        return self.driver.current_url

    def click_order_button_in_head(self):
        wait = WebDriverWait(self.driver, 3)
        self.driver.find_element(
            *base_page_locators.order_form_button_in_head).click()
        wait.until(expected_conditions.presence_of_element_located(
            order_page_locators.for_whom_scooter_header))

    def go_to_main_page(self):
        wait = WebDriverWait(self.driver, 3)
        self.driver.get(configuration.URL)
        # wait.until(expected_conditions.url_to_be(
        #     configuration.URL))
