from selenium import webdriver
import pytest
import configuration
import test_data


@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Firefox()
    driver.get(configuration.URL)
    driver.add_cookie(test_data.cookies)
    driver.refresh()
    yield driver
    driver.quit()
