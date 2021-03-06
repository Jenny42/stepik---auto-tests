from selenium import webdriver
import time
import os


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Jenny")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Sys")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("mail@mail.ru")
    
    file = browser.find_element_by_name("file") 
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'les2.2-step7-file.txt')           # добавляем к этому пути имя файла 
    file.send_keys(file_path)
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("button = document.getElementsByTagName(\"button\")[0];button.scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()