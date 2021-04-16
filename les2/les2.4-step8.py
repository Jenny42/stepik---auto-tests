from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import pyperclip

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"),"$100")
        )
    
    button = browser.find_element_by_id("book")
    button.click()
    
    x_txt = browser.find_element_by_id("input_value")
    x = x_txt.text
    y = calc(x) 
    
    answer = browser.find_element_by_css_selector("#answer") 
    answer.send_keys(y)
    
    # Отправляем заполненную форму
    button1 = browser.find_element_by_id("solve")
    button1.click()
    
    alert1 = browser.switch_to.alert
    alert_text = alert1.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()