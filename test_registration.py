import time
import unittest

from selenium import webdriver


class MyTestCase(unittest.TestCase):
    def test_something(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome(executable_path="C://Users//Kozlova.E//drivers//chromedriver.exe")
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            elements = browser.find_elements_by_css_selector('.first_block input')
            for element in elements:
                element.send_keys("111")

            # Отправляем заполненную форму
            button = browser.find_element_by_css_selector(".btn btn-default")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(5)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual ("Congratulations! You have successfully registered!", welcome_text)

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(5)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == '__main__':
    unittest.main()
