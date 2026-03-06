from pages.base_page import BasePage


class HomeFaqPage(BasePage):

    def click_question_button(self, question, answer):
        self.scroll_to_element(question)
        self.wait_element_to_clickable(question)
        self.click_to_element(question)
        self.wait_visibility_of_element(answer)
