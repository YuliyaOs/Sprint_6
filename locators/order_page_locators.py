from selenium.webdriver.common.by import By

order_form_button_middle_page = [
    By.XPATH, "(.//button[text()='Заказать'])[2]"]
for_whom_scooter_header = [By.XPATH, ".//div[text()='Для кого самокат']"]
name_input = [By.XPATH, ".//input[contains(@placeholder, 'Имя')]"]
surname_input = [By.XPATH, ".//input[contains(@placeholder, 'Фамилия')]"]
address_input = [By.XPATH, ".//input[contains(@placeholder, 'Адрес')]"]
metro_station_input = [
    By.XPATH, ".//input[contains(@placeholder, 'Станция')]"]
phone_input = [By.XPATH, ".//input[contains(@placeholder, 'Телефон')]"]
next_button = [By.XPATH, ".//button[text()='Далее']"]
about_renting_header = [By.XPATH, ".//div[text()='Про аренду']"]
when_input = [By.XPATH, ".//input[contains(@placeholder, 'Когда')]"]
rental_period_open = [By.XPATH, ".//div[contains(text(), 'Срок')]"]
rental_period_day = [By.XPATH, ".//div[contains(text(), 'сутки')]"]
color_scooter_black = [By.XPATH, ".//label/input[@id='black']"]
comment_input = [
    By.XPATH, ".//input[contains(@placeholder, 'Комментарий')]"]
order_button = [By.XPATH, "(.//button[text()='Заказать'])[2]"]
order_modal_header = [By.XPATH, ".//div[text()='Хотите оформить заказ?']"]
yes_button = [By.XPATH, ".//button[text()='Да']"]
rcc_confirm_button = [By.XPATH, ".//button[@id='rcc-confirm-button']"]
order_number = [By.XPATH, ".//div[contains(text(),'Номер заказа')]"]
view_status_button = [By.XPATH, ".//button[text()='Посмотреть статус']"]
