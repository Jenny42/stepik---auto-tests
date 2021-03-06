from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #x_txt = browser.find_element_by_id("input_value")
    treasure = browser.find_element_by_id("treasure") 
    x = treasure.get_attribute("valuex");
    y = calc(x) 
    
    
    answer = browser.find_element_by_id("answer") 
    answer.send_keys(y)
    
    #chk = browser.find_element_by_css_selector("#robotCheckbox") 
    chk = browser.find_element_by_id("robotCheckbox") 
    chk.click()
    
    rbt = browser.find_element_by_id("robotsRule") 
    rbt.click()
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()