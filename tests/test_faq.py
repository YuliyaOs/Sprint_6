from selenium import webdriver
from pages.home_faq_page import HomeFaqPage


class TestFAQ:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://qa-scooter.praktikum-services.ru/')
        cls.driver.refresh()

    def test_question_1(self):
        home_page = HomeFaqPage(self.driver)
        home_page.click_question_button(*home_page.question_1)
        home_page.wait_answer(home_page.answer_1)

        assert home_page.get_answer(*home_page.answer_1
                                    ).text == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    def test_question_2(self):
        home_page = HomeFaqPage(self.driver)
        home_page.click_question_button(*home_page.question_2)
        home_page.wait_answer(home_page.answer_2)

        assert home_page.get_answer(*home_page.answer_2
                                    ).text == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    def test_question_3(self):
        home_page = HomeFaqPage(self.driver)
        home_page.click_question_button(*home_page.question_3)
        home_page.wait_answer(home_page.answer_3)

        assert home_page.get_answer(
            *home_page.answer_3).text == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    def test_question_4(self):
        home_page = HomeFaqPage(self.driver)
        home_page.click_question_button(*home_page.question_4)
        home_page.wait_answer(home_page.answer_4)

        assert home_page.get_answer(
            *home_page.answer_4).text == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    def test_question_5(self):
        home_page = HomeFaqPage(self.driver)
        home_page.click_question_button(*home_page.question_5)
        home_page.wait_answer(home_page.answer_5)

        assert home_page.get_answer(
            *home_page.answer_5).text == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    def test_question_6(self):
        home_page = HomeFaqPage(self.driver)
        home_page.click_question_button(*home_page.question_6)
        home_page.wait_answer(home_page.answer_6)

        assert home_page.get_answer(
            *home_page.answer_6).text == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    def test_question_7(self):
        home_page = HomeFaqPage(self.driver)
        home_page.click_question_button(*home_page.question_7)
        home_page.wait_answer(home_page.answer_7)

        assert home_page.get_answer(
            *home_page.answer_7).text == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    def test_question_8(self):
        home_page = HomeFaqPage(self.driver)
        home_page.click_question_button(*home_page.question_8)
        home_page.wait_answer(home_page.answer_8)

        assert home_page.get_answer(
            *home_page.answer_8).text == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
