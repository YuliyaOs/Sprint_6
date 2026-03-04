from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pages.base_page as base_page


class HomeFaqPage(base_page.BasePage):

    def click_question_button(self, *question):
        element = self.driver.find_element(*question)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(question))
        self.driver.find_element(*question).click()

    def wait_answer(self, answer):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(answer))

    def get_answer(self, *answer):
        return self.driver.find_element(*answer)
