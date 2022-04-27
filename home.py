from selenium.webdriver.common.by import By
import time
from selenium import webdriver
driver = webdriver.Chrome()

# Открываем сайт
driver.maximize_window()
driver.implicitly_wait(5)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
driver.get("http://practice.automationtesting.in")
time.sleep(2)

# Прокручиваем страницу на 800 пикселей
driver.execute_script("window.scrollBy(0, 800);")
time.sleep(1)

# Открываем страницу книги Selenium Ruby
Sel_Ruby_btn = driver.find_element(By.CSS_SELECTOR, 'a > [title="Selenium Ruby"]')
Sel_Ruby_btn.click()
time.sleep(1)

# Прокручиваем страницу на 300 пикселей
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(1)

# Открываем вкладку Reviews
Reviews_tab = driver.find_element(By.CSS_SELECTOR, 'li > [href="#tab-reviews"]')
Reviews_tab.click()
time.sleep(1)

# Прокручиваем страницу на 300 пикселей
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(2)

# Ставим рейтинг 5 звезд
raiting_btn = driver.find_element(By.CLASS_NAME, "star-5")
raiting_btn.click()
time.sleep(1)

# Прокручиваем страницу на 300 пикселей
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(1)

# Заполняем поле Review
Reviews_edit = driver.find_element(By.ID, "comment")
Reviews_edit.send_keys("Nice book!")
time.sleep(1)

# Заполняем Name
name = driver.find_element(By.ID, "author")
name.send_keys("Admin")
time.sleep(1)

# Заполняем Email
email = driver.find_element(By.ID, "email")
email.send_keys("admin@mail.ru")
time.sleep(1)

# Сохраняем отзыв
submit_btn = driver.find_element(By.CLASS_NAME, "submit")
submit_btn.click()
time.sleep(1)

# Закрываем браузер
time.sleep(2)
driver.quit()