import time
import math
import os 

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/file_input.html")

# поис полей FirstName, LastName, Email и внесение в них информации
textInputFirstName = driver.find_elements_by_css_selector("[name='firstname']")
textInputFirstName[0].send_keys("Anastasia")

textInputLastName = driver.find_elements_by_css_selector("[name='lastname']")
textInputLastName[0].send_keys("Shushlebina")

textInputEmail = driver.find_elements_by_css_selector("[name='email']")
textInputEmail[0].send_keys("nastya_kysia@mail.ru")

time.sleep(1)

# Найдем кнопку "выбирете файл"
btnLoadFile = driver.find_elements_by_css_selector("[type='file']") 
# получаем путь к директории текущего исполняемого файла 
currentDir = os.path.abspath(os.path.dirname(__file__))
# добавляем к этому пути имя файла 
filePath = os.path.join(currentDir, '1.txt')

btnLoadFile[0].send_keys(filePath)

# Найдем кнопку submit
btnSubmit = driver.find_element_by_css_selector(".btn") 
btnSubmit.click()

time.sleep(5)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()