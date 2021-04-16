from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/find_link_text" 
text = str(math.ceil(math.pow(math.pi, math.e)*10000)) #224592

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    link2 = browser.find_element_by_link_text(text)
    link2.click()

    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Jenny")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Sys")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Krasnoyarsk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
    driver.close()
    time.sleep(2)
    driver.quit()

# не забываем оставить пустую строку в конце файла
