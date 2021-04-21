from selenium import webdriver
import time
import unittest


      
class TestAbs(unittest.TestCase):
    def setUp(self):
      self.driver = webdriver.Chrome()
    
    def find_text(self, link):
      browser = self.driver
      browser.get(link)
      # говорим WebDriver ждать все элементы в течение 5 секунд
      browser.implicitly_wait(5)

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
      
      # записываем в переменную welcome_text текст из элемента welcome_text_elt
      return browser.find_element_by_tag_name("h1").text      
    
    def test_abs1(self):
      welcome_text = self.find_text("http://suninjuly.github.io/registration1.html")
      # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
      self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Sorry! You are not registered!")

     
    def test_abs2(self):
      welcome_text2 = self.find_text("http://suninjuly.github.io/registration2.html")
      # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
      self.assertEqual(welcome_text2, "Congratulations! You have successfully registered!", "Sorry! You are not registered!")
      
    def quitBrouser(self):
      # закрываем браузер после всех манипуляций
      self.driver.quit()
        
if __name__ == "__main__":
    unittest.main()