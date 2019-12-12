import time
import math

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока стоимость не стнет равной $100
waitPrice = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID,"price"), "$100")
    )

# поис кнопки "Book"
btnBook = driver.find_elements_by_id("book")
btnBook[0].click()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Считываем значение х
x = driver.find_element_by_id("input_value").text
y = calc(x)

# Ищем поле для ввода ответа
textInputAnswer = driver.find_element_by_id("answer")
textInputAnswer.send_keys(y)

# Найдем кнопку submit
btnSubmit = driver.find_element_by_id("solve") 
btnSubmit.click()

time.sleep(5)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()