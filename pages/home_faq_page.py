from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class HomeFaqPage:

    question_1 = [
        By.XPATH, ".//div[contains(text(),'Сколько это стоит? И как оплатить?')]"]
    question_2 = [
        By.XPATH, ".//div[contains(text(),'Хочу сразу несколько самокатов! Так можно?')]"]
    question_3 = [
        By.XPATH, ".//div[contains(text(),'Как рассчитывается время аренды?')]"]
    question_4 = [
        By.XPATH, ".//div[contains(text(),'Можно ли заказать самокат прямо на сегодня?')]"]
    question_5 = [
        By.XPATH, ".//div[contains(text(),'Можно ли продлить заказ или вернуть самокат раньше?')]"]
    question_6 = [
        By.XPATH, ".//div[contains(text(),'Вы привозите зарядку вместе с самокатом?')]"]
    question_7 = [
        By.XPATH, ".//div[contains(text(),'Можно ли отменить заказ?')]"]
    question_8 = [
        By.XPATH, ".//div[contains(text(),'Я жизу за МКАДом, привезёте?')]"]

    answer_1 = [By.XPATH, question_1[1]+'/following::div[1]']
    answer_2 = [By.XPATH, question_2[1]+'/following::div[1]']
    answer_3 = [By.XPATH, question_3[1]+'/following::div[1]']
    answer_4 = [By.XPATH, question_4[1]+'/following::div[1]']
    answer_5 = [By.XPATH, question_5[1]+'/following::div[1]']
    answer_6 = [By.XPATH, question_6[1]+'/following::div[1]']
    answer_7 = [By.XPATH, question_7[1]+'/following::div[1]']
    answer_8 = [By.XPATH, question_8[1]+'/following::div[1]']

    def __init__(self, driver):
        self.driver = driver

    def click_question_button(self, *question):
        element = self.driver.find_element(*self.question_6)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(question))
        self.driver.find_element(*question).click()

    def wait_answer(self, answer):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(answer))

    def get_answer(self, *answer):
        return self.driver.find_element(*answer)
