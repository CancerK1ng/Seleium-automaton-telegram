# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.common.keys import Keys
#
#
# drivers = webdriver.Chrome()
# drivers.get('https://web.telegram.org/k/')
# drivers.maximize_window()
# time.sleep(3)
# # search = drivers.find_element(By.XPATH, '//div[normalize-space()="Search"]')
# # search.send_keys('SMM')
# log_in = drivers.find_element(By.XPATH, '//div[normalize-space()="Log in by phone Number"]')
# log_in.click()
# time.sleep(2)
# wr_number = drivers.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]")
# wr_number.send_keys('7778480527')
#
# time.sleep(5)
# n_button = drivers.find_element(By.XPATH, '//button[normalize-space()="Next"]')
# n_button.click()
# cod_verify = drivers.find_element(By.NAME, '7330278707404238')
# cod_verify.send_keys(input('Код подтверждения:'))
# time.sleep(5)
# Search = drivers.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]')
# Search.send_keys('Amir Akhmetzhanov')
# Amir = drivers.find_element(By.XPATH,"//div[@class='search-group search-group-contacts']//div[@class='c-ripple']")
# Amir.click()
# mesg = drivers.find_element(By.XPATH, "//div[@class='input-message-input scrollable scrollable-y i18n no-scrollbar']")
# mesg.send_keys('Давай курить, это Я - программа по автоматизаций жизненных процессов)')
# send_mesg = drivers.find_element(By.XPATH, "//div[@class='c-ripple']" )
# send_mesg.click()
# # Close the driver
# drivers.close()

# def login():
#     print("Connecting to Telegram Web, please wait")
#
#     browser = webdriver.Chrome()
#
#
#     browser.get("https://web.telegram.org/#/login")
#
#     time.sleep(3)
#
#     phone_input_code = browser.find_element(By.NAME, "Country")
#     phone_input_number = browser.find_element(By.NAME, "Phone_number")
#
#     country_code = input("Country code: ")
#     phone_number = input("Phone number: ")
#
#     phone_input_code.send_keys(Keys.BACKSPACE + Keys.BACKSPACE + country_code + Keys.ENTER)
#     phone_input_number.send_keys(Keys.BACKSPACE + phone_number + Keys.ENTER)
#
#     # Wait for the page to load
#     time.sleep(5)
#
#     confirm_input = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div[4]/input")
#     confirm_code = input("Confirmation code (sent via SMS): ")
#     confirm_input.send_keys(confirm_code + Keys.ENTER)
#
#     time.sleep(5)
#     password_input = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/form/div[1]/input")
#     password_send = input("Please Login Password:")
#     password_input.send_keys(password_send + Keys.ENTER)
#     return browser
# login()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


drivers = webdriver.Chrome()
drivers.get('https://web.telegram.org/k/')
drivers.maximize_window()
time.sleep(10)

# log_in = drivers.find_element(By.XPATH, '//div[normalize-space()="Log in by phone Number"]')
# log_in.click()
# time.sleep(2)
# wr_number = drivers.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/div[1]")
# wr_number.send_keys('7778480527')

# n_button = drivers.find_element(By.XPATH, '//button[normalize-space()="Next"]')
# n_button.click()
# cod_verify = drivers.find_element(By.NAME, '7330278707404238')
# cod_verify.send_keys(input('Код подтверждения:'))
# time.sleep(5)
Search = drivers.find_element(By.XPATH, "//div[@class='btn-icon rp btn-menu-toggle sidebar-tools-button is-visible']//div[@class='c-ripple']")
Search.click()
time.sleep(2)
Search1 = drivers.find_element(By.XPATH, "//div[@class='btn-menu-item rp-overflow tgico-user']")
Search1.click()
time.sleep(2)
Search2 = drivers.find_element(By.XPATH, "//div[@id='contacts-container']//input[@placeholder='Search']")
Search2.send_keys('Amir Akhmetzhanov')
time.sleep(2)
Amir = drivers.find_element(By.XPATH, "//ul[@id='contacts']//div[@class='c-ripple']")
Amir.click()
time.sleep(2)
mesg = drivers.find_element(By.XPATH, "//div[@class='input-message-input scrollable scrollable-y i18n no-scrollbar']")
mesg.send_keys('Давай курить, это Я - программа по автоматизаций жизненных процессов)')
time.sleep(2)
send_mesg = drivers.find_element(By.XPATH, "//button[@class='btn-icon tgico-none btn-circle z-depth-1 btn-send animated-button-icon rp send']" )
send_mesg.click()
time.sleep(10)
# Close the driver
drivers.close()