from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_txt = browser.find_element_by_id("input_value")
    x = x_txt.text
    y = calc(x) 
    
    answer = browser.find_element_by_css_selector("#answer") 
    answer.send_keys(y)
    
    #chk = browser.find_element_by_css_selector("#robotCheckbox") 
    chk = browser.find_element_by_id("robotCheckbox") 
    chk.click()
    
    rbt = browser.find_element_by_id("robotsRule") 
    browser.execute_script("rbt = document.getElementById(\"robotsRule\");rbt.scrollIntoView(true);", rbt)
    rbt.click()
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("button = document.getElementsByTagName(\"button\")[0];button.scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()