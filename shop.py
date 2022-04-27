from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()

# Открываем сайт
driver.maximize_window()
wait = WebDriverWait(driver, 20)
driver.implicitly_wait(5)
first_browser_tab = driver.window_handles[0]
driver.switch_to.window(first_browser_tab)
driver.get("http://practice.automationtesting.in")
time.sleep(2)

# Выполняем вход
## my_account_tab = driver.find_element(By.LINK_TEXT, "My Account")
# my_account_tab.click()
# time.sleep(1)
# login = driver.find_element(By.ID, "username")
# login.send_keys("admin@mail.ru")
# time.sleep(1)
# password = driver.find_element(By.ID, "password")
# password.send_keys("Koly@masta")
# time.sleep(1)
# log_btn = driver.find_element(By.NAME, "login")
# log_btn.click()
# time.sleep(1)

# Нажимаем на вкладку Shop
shop_tab = driver.find_element(By.LINK_TEXT, "Shop")
shop_tab.click()
time.sleep(1)
################################### Отображение страницы товара
# # Открываем страницу книги HTML5 Forms
# HTML5_Forms_book = driver.find_element(By.CSS_SELECTOR, ".post-181 > a > h3")
# HTML5_Forms_book.click()
# time.sleep(1)
#
# # Проверка, что заголовок книги называется "HTML5 Forms"
# html5 = wait.until(EC. text_to_be_present_in_element((By.CLASS_NAME, "entry-title"), "HTML5 Forms"))
# print('Заголовок книги называется "HTML5 Forms"')

#################################### Количество товаров в категории
#
# # Открываем категорию HTML
# html_category = driver.find_element(By.LINK_TEXT, "HTML")
# html_category.click()
# time.sleep(1)
#
# # Проверка, что на странице отображается 3 товара
# element_1 = wait.until(EC. text_to_be_present_in_element((By.CSS_SELECTOR, ".post-181 > a > h3"), "HTML5 Forms"))
# element_2 = wait.until(EC. text_to_be_present_in_element((By.CSS_SELECTOR, ".post-182 > a > h3"), "HTML5 WebApp Develpment"))
# element_3 = wait.until(EC. text_to_be_present_in_element((By.CSS_SELECTOR, ".post-163 > a > h3"), "Thinking in HTML"))
# print("На странице отображается 3 товара")

#################################### Сортировка товаров
#
# # Проверка, что выбрана сортировка по умолчанию
# print("Проверка выбора сортировки:")
# sorting = driver.find_element(By.CLASS_NAME, "orderby")
# sorting_check = sorting.get_attribute("value")
# assert sorting_check == "menu_order"
# print("Выбрана сортировка по умолчанию")
# time.sleep(1)
#
# # Выбираем сортировку по цене от большей к меньшей
# select = Select(sorting)
# select.select_by_value("price-desc")
# time.sleep(1)
#
# # Снова объявляем переменную с локатором основного селектора сортировки
# sorting = driver.find_element(By.CLASS_NAME, "orderby")
#
# # Проверка, что выбрана сортировка по цене от большей к меньшей
# print("Проверка выбора сортировки:")
# sorting = driver.find_element(By.CLASS_NAME, "orderby")
# sorting_check = sorting.get_attribute("value")
# assert sorting_check == "price-desc"
# print("Выбрана сортировка по цене от большей к меньшей")
# time.sleep(1)

#################################### Отображение, скидка товара
# Открываем страницу товара Android quick start guide
# AQSG = driver.find_element(By.CSS_SELECTOR, ".post-169 > a > h3")
# AQSG.click()
# time.sleep(1)
#
# # Проверка, что старая цена равна ₹600
# old_price = driver.find_element(By.CSS_SELECTOR, ".price > del > span")
# old_price_get_text = old_price.text
# assert old_price_get_text == "₹600.00"
# print("Старая цена товара:", old_price_get_text)
#
# # Проверка, что новая цена равна ₹450
# new_price = driver.find_element(By.CSS_SELECTOR, ".price > ins > span")
# new_price_get_text = new_price.text
# assert new_price_get_text == "₹450.00"
# print("Новая цена товара:", new_price_get_text)
#
# # Открытие предпросмотра обложки книги
# book_cover_open = wait.until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[title="Android Quick Start Guide"]'))).click()
#
# # Закрытие предпросмотра обложки книги
# book_cover_close = wait.until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))).click()

#################################### Проверка цены в корзине
# # Добавляем в корзину книгу "HTML5 WebApp Develpment"
# adding_to_cart = driver.find_element(By.CSS_SELECTOR, 'a[data-product_id="182"]')
# adding_to_cart.click()
# time.sleep(2)
#
# # Проверка, что в корзине 1 товар
# cart_item = driver.find_element(By.CLASS_NAME, "cartcontents")
# cart_item_check = cart_item.text
# assert cart_item_check == "1 Item"
# print("В корзине находится 1 товар")
#
# # Проверка, что цена товара равна ₹180.00
# cart_price = driver.find_element(By.CSS_SELECTOR, "#wpmenucartli > a > .amount")
# cart_price_check = cart_price.text
# assert cart_price_check == "₹180.00"
# print("Цена товара: ₹180.00")
#
# # Открываем корзину
# cart = driver.find_element(By.CLASS_NAME, "wpmenucart-contents")
# cart.click()
# time.sleep(1)
#
# # Проверка, что в Subtotal отобразилась стоимость
# subtotal_price = wait.until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal > td"), "₹180.00"))
# print("Subtotal: ₹180.00")
#
# # Проверка, что в Total отобразилась стоимость
# total_price = wait.until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total > td"), "₹189.00"))
# print("Total: ₹189.00")

#################################### Работа в корзине
# # Проскролим вниз на 300 пикселей
# driver.execute_script("window.scrollBy(0, 300);")
# time.sleep(1)
#
# # Добавляем в корзину книгу "HTML5 WebApp Develpment"
# HTML5_book = driver.find_element(By.CSS_SELECTOR, 'a[data-product_id="182"]')
# HTML5_book.click()
# time.sleep(2)
#
# # Добавляем в корзину книгу "JS Data Structures and Algorithm"
# JS_Data_book = driver.find_element(By.CSS_SELECTOR, 'a[data-product_id="180"]')
# JS_Data_book.click()
# time.sleep(2)
#
# # Открываем корзину
# cart = driver.find_element(By.CLASS_NAME, "wpmenucart-contents")
# cart.click()
# time.sleep(2)
#
# # Удаляем первую книгу
# remove_item = driver.find_element(By.CSS_SELECTOR, '.product-remove > [data-product_id="182"]')
# remove_item.click()
# time.sleep(2)
#
# # Отмена удаления
# undo_btn = driver.find_element(By.CSS_SELECTOR, '.woocommerce-message > a')
# undo_btn.click()
# time.sleep(2)
#
# # Очистка поля ввода количества товара
# quantity = driver.find_element(By.CSS_SELECTOR, '.cart_item:nth-child(1) > td > .quantity > input')
# quantity.clear()
#
# # В Quantity увеличиваем количесто товара до 3 шт для "JS Data Structures and Algorithm“
# quantity.send_keys("3")
# time.sleep(1)
#
# # Нажимаем на кнопку "UPDATE BASKET"
# update_basket = driver.find_element(By.CSS_SELECTOR, 'input[value="Update Basket"]')
# update_basket.click()
# time.sleep(2)
#
# # Проверка, что value элемента quantity для "JS Data Structures and Algorithm" равно 3
# quantity = driver.find_element(By.CSS_SELECTOR, '.cart_item:nth-child(1) > td > .quantity > input')
# quantity_check = quantity.get_attribute("value")
# assert quantity_check == "3"
# print('Value элемента quantity для "JS Data Structures and Algorithm" равно 3')
# time.sleep(2)
#
# # Нажимаем на кнопку Apply Coupon
# apply_btn = driver.find_element(By.CSS_SELECTOR, '[value="Apply Coupon"]')
# apply_btn.click()
# time.sleep(2)
#
# # Проверка, что возникло сообщение Please enter a coupon code.
# error = driver.find_element(By.CLASS_NAME, "woocommerce-error")
# error_check = error.text
# assert error_check == "Please enter a coupon code."
# print("Возникло сообщение об ошибке: Please enter a coupon code.")

#################################### Покупка товара
# Проскролим вниз на 300 пикселей
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(1)

# Добавляем в корзину книгу "HTML5 WebApp Develpment"
HTML5_book = driver.find_element(By.CSS_SELECTOR, 'a[data-product_id="182"]')
HTML5_book.click()
time.sleep(2)

# Открываем корзину
cart = driver.find_element(By.CLASS_NAME, "wpmenucart-contents")
cart.click()
time.sleep(2)

# Нажимаем на "PROCEED TO CHECKOUT"
checkout_btn = wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")))
checkout_btn.click()
time.sleep(2)

# Добавляем явное ожидание
label = wait.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[for="billing_first_name"]'), "First Name"))

# заполняем все обязательные поля
first_name = driver.find_element(By.ID, "billing_first_name")
first_name.send_keys("Firstname")
time.sleep(1)
last_name = driver.find_element(By.ID, "billing_last_name")
last_name.send_keys("Lastname")
time.sleep(1)
email = driver.find_element(By.ID, "billing_email")
email.send_keys("admin@mail.ru")
time.sleep(1)
phone = driver.find_element(By.ID, "billing_phone")
phone.send_keys("11111111111")
time.sleep(1)
country = driver.find_element(By.CLASS_NAME, "select2-arrow")
country.click()
time.sleep(1)
country_place = driver.find_element(By.CLASS_NAME, "select2-input")
country_place.send_keys("Russia")
time.sleep(1)
russia_select = driver.find_element(By.CLASS_NAME, "select2-match")
russia_select.click()
time.sleep(1)
street_address1 = driver.find_element(By.ID, "billing_address_1")
street_address1.send_keys("Street")
time.sleep(1)
street_address2 = driver.find_element(By.ID, "billing_address_2")
street_address2.send_keys("Appartment")
time.sleep(1)
city = driver.find_element(By.ID, "billing_city")
city.send_keys("City")
time.sleep(1)
state = driver.find_element(By.ID, "billing_state")
state.send_keys("State")
time.sleep(1)
postcode = driver.find_element(By.ID, "billing_postcode")
postcode.send_keys("111111")
time.sleep(1)

# Проскролим вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(1)

# Выбираем спосоь оплаты "Check Payments"
check_payments = driver.find_element(By.ID, "payment_method_cheque")
check_payments.click()
time.sleep(2)

# Нажимаем кнопку PLACE ORDER
place_order_btn = wait.until(EC.element_to_be_clickable((By.ID, "place_order")))
place_order_btn.click()

# Проверка, что отображается надпись "Thank you. Your order has been received."
inscription = wait.until(EC.text_to_be_present_in_element((
        By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
print('Появилась надпись: "Thank you. Your order has been received."')

# Проверка, что в Payment Method отображается текст "Check Payments"
payment_method = wait.until(EC.text_to_be_present_in_element((
        By.CSS_SELECTOR, '.shop_table.order_details > tfoot > tr:nth-child(3) > td'), "Check Payments"))
print('Payment method: Check Payments')

# Закрываем браузер
time.sleep(2)
driver.quit()