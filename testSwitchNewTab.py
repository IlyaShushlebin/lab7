import time
import math

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/redirect_accept.html")
time.sleep(5)

# поис кнопки "I want to go on a magical journey!
btn = driver.find_elements_by_css_selector(".btn")
btn[0].click()

# переход на вторую вкладку
driver.switch_to.window(driver.window_handles[1])

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Считываем значение х
x = driver.find_element_by_id("input_value").text
y = calc(x)

# Ищем поле для ввода ответа
textInputAnswer = driver.find_element_by_id("answer")
textInputAnswer.send_keys(y)

# Найдем кнопку submit
btnSubmit = driver.find_element_by_css_selector(".btn") 
btnSubmit.click()

time.sleep(5)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()