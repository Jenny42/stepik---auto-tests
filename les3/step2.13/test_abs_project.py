from selenium import webdriver
import time
import unittest

def find_text(link):
      browser = webdriver.Chrome()
      browser.get(link)

      # Ваш код, который заполняет обязательные поля
      input_first = browser.find_element_by_css_selector(".first:required") #псевдокласс
      input_first.send_keys("Jenny")
      input_second = browser.find_element_by_css_selector(".second[required]") #атрибут
      input_second.send_keys("Sys")
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
      # ожидание чтобы визуально оценить результаты прохождения скрипта
      time.sleep(5)
      # закрываем браузер после всех манипуляций
      browser.quit()
      
      return welcome_text
      
class TestAbs(unittest.TestCase):
      
    
    def test_abs1(self):
      welcome_text = find_text("http://suninjuly.github.io/registration1.html")
      # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
      self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Sorry! You are not registered!")

     
    def test_abs2(self):
      welcome_text2 = find_text("http://suninjuly.github.io/registration2.html")
      # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
      self.assertEqual(welcome_text2, "Congratulations! You have successfully registered!", "Sorry! You are not registered!")
        
if __name__ == "__main__":
    unittest.main()