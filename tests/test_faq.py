from pages.home_faq_page import HomeFaqPage
from locators import home_faq_page_locators


class TestFaq:

    def test_question_1(self, driver):
        home_page = HomeFaqPage(driver)
        home_page.click_question_button(
            home_faq_page_locators.question_1, home_faq_page_locators.answer_1)

        assert home_page.find_element(home_faq_page_locators.answer_1
                                      ).is_displayed()

    def test_question_2(self, driver):
        home_page = HomeFaqPage(driver)
        home_page.click_question_button(
            home_faq_page_locators.question_2, home_faq_page_locators.answer_2)

        assert home_page.find_element(home_faq_page_locators.answer_2
                                      ).is_displayed()

    def test_question_3(self, driver):
        home_page = HomeFaqPage(driver)
        home_page.click_question_button(
            home_faq_page_locators.question_3, home_faq_page_locators.answer_3)

        assert home_page.find_element(
            home_faq_page_locators.answer_3).is_displayed()

    def test_question_4(self, driver):
        home_page = HomeFaqPage(driver)
        home_page.click_question_button(
            home_faq_page_locators.question_4, home_faq_page_locators.answer_4)

        assert home_page.find_element(
            home_faq_page_locators.answer_4).is_displayed()

    def test_question_5(self, driver):
        home_page = HomeFaqPage(driver)
        home_page.click_question_button(
            home_faq_page_locators.question_5, home_faq_page_locators.answer_5)

        assert home_page.find_element(
            home_faq_page_locators.answer_5).is_displayed()

    def test_question_6(self, driver):
        home_page = HomeFaqPage(driver)
        home_page.click_question_button(
            home_faq_page_locators.question_6, home_faq_page_locators.answer_6)

        assert home_page.find_element(
            home_faq_page_locators.answer_6).is_displayed()

    def test_question_7(self, driver):
        home_page = HomeFaqPage(driver)
        home_page.click_question_button(
            home_faq_page_locators.question_7, home_faq_page_locators.answer_7)

        assert home_page.find_element(
            home_faq_page_locators.answer_7).is_displayed()

    def test_question_8(self, driver):
        home_page = HomeFaqPage(driver)
        home_page.click_question_button(
            home_faq_page_locators.question_8, home_faq_page_locators.answer_8)

        assert home_page.find_element(
            home_faq_page_locators.answer_8).is_displayed()
