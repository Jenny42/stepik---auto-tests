from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    #elements = browser.find_elements_by_css_selector("input[required]")
    #for element in elements:
    #   element.send_keys("Мой ответ")
    #Ниже эксперименты с селекторами. Можно использовать, что нравится.
    input_first = browser.find_element_by_css_selector(".first:required") #псевдокласс
    input_first.send_keys("Jenny")
    input_second = browser.find_element_by_css_selector(".second[required]") #атрибут
    input_second.send_keys("Sys")
    #input_third = browser.find_element_by_css_selector(".third[required]")
    #input_third.send_keys("mail@mail.ru")
    
    #input_first = browser.find_element_by_xpath("//input[contains(@class,'first') and @required]")
    #input_first.send_keys("Jenny")
    #input_second = browser.find_element_by_xpath("//input[contains(@class,'second') and @required]")
    #input_second.send_keys("Sys")
    input_third = browser.find_element_by_xpath("//input[contains(@class,'third') and @required]") #xpath
    input_third.send_keys("mail@mail.ru")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()