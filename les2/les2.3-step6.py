from selenium import webdriver
import time
import math
import pyperclip

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x_txt = browser.find_element_by_id("input_value")
    x = x_txt.text
    y = calc(x) 
    
    answer = browser.find_element_by_css_selector("#answer") 
    answer.send_keys(y)
    
    # Отправляем заполненную форму
    button1 = browser.find_element_by_css_selector("button.btn")
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