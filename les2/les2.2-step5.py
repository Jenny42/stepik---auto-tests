from selenium import webdriver
import time

try: 
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("button = document.getElementsByTagName(\"button\")[0];button.scrollIntoView(true);", button)
    button.click()
    
    
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()