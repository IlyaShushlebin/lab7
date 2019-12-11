import time
import math

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/execute_script.html")

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Считываем значение х у элемента img с атрибутом valuex
x = driver.find_element_by_id("input_value").text
y = calc(x)

# скролим страницу вниз на 160px, чтобы стала видна кнопка Submit
driver.execute_script("window.scrollBy(0,160)")

# Ищем поле для ввода текста
textinput = driver.find_element_by_id("answer")
# Запись текста для поиска в найденное поле
textinput.send_keys(y)

# Отмечаем checkbox "I'm the robot"
chkIRobot = driver.find_elements_by_id("robotCheckbox")
chkIRobot[0].click()

time.sleep(1)

# Выбираем radiobutton "Robots rule!".
rbnRobotsRule = driver.find_elements_by_id("robotsRule")
rbnRobotsRule[0].click()

time.sleep(1)

# Найдем кнопк submit
btnSubmit = driver.find_element_by_css_selector(".btn") 
btnSubmit.click()

time.sleep(5)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()