import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

from selenium.webdriver.support.ui import Select

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome("C:/chromedriver/chromedriver.exe")

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://suninjuly.github.io/selects1.html")
time.sleep(1)

def sum(x1,x2):
  return str(int(x1)+int(x2))

# Считываем значение num1 и num2 и подсчитываем их сумму
num1 = driver.find_elements_by_id("num1")[0].text
num2 = driver.find_elements_by_id("num2")[0].text
y=sum(num1, num2)

# Выбираем из выпадающего списка результат суммы
select = Select(driver.find_element_by_tag_name("select"))
select.select_by_value(y)

time.sleep(1)

# Найдем кнопку submit
btnSubmit = driver.find_element_by_css_selector(".btn") 
btnSubmit.click()

time.sleep(5)

# После выполнения всех действий мы не должны забыть закрыть окно браузера
driver.quit()