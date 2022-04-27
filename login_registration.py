from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()

# Открываем сайт
driver.maximize_window()
driver.implicitly_wait(5)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
driver.get("http://practice.automationtesting.in")
time.sleep(2)

# Нажимаем на вкладку "My Account"
my_account_tab = driver.find_element(By.LINK_TEXT, "My Account")
my_account_tab.click()
time.sleep(1)

# # В разделе "Register", введем email для регистрации
# email = driver.find_element(By.ID, "reg_email")
# email.send_keys("admin@mail.ru")
# time.sleep(1)
#
# # В разделе "Register", введем пароль для регистрации
# password = driver.find_element(By.ID, "reg_password")
# password.send_keys("Koly@masta")
# time.sleep(1)
#
# # Нажимаем кнопку Register
# reg_btn = driver.find_element(By.NAME, "register")
# reg_btn.click()
# time.sleep(1)

# Ввод логина
login = driver.find_element(By.ID, "username")
login.send_keys("admin@mail.ru")
time.sleep(1)

# Ввод пароля
password = driver.find_element(By.ID, "password")
password.send_keys("Koly@masta")
time.sleep(1)

# Нажимаем кнопку Login
log_btn = driver.find_element(By.NAME, "login")
log_btn.click()
time.sleep(1)

# Проверка, что на странице есть элемент logout
wait = WebDriverWait(driver, 10)
logout = wait.until(
    EC. text_to_be_present_in_element((By.CSS_SELECTOR, 'li > [href="http://practice.automationtesting.in/my-account/customer-logout/"]'), "Logout"))
print('На странице есть элемент "Logout"')

# Закрываем браузер
time.sleep(2)
driver.quit()
