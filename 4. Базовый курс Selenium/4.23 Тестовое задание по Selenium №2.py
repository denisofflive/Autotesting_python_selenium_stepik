import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
base_url = 'https://demoqa.com/date-picker'
driver.get(base_url)
driver.maximize_window()

"""New date +10 days'"""
now_date = datetime.datetime.utcnow().strftime("%m/%d/%Y")
print(now_date)
list_date = now_date.split('/')
month = list_date[0]
year = list_date[2]
new_day = int(list_date[1]) + 10

# високосный год
if month == '02' and new_day > 29 and ((int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0):
    month = ''.join('0') + str(int(list_date[0]) + 1)
    new_day = int(new_day - 29)
    if 1 < new_day < 10:
        new_day = ''.join('0') + str(new_day)
else:  # невисокосный год
    if month == '02' and new_day > 28:
        month = ''.join('0') + str(int(list_date[0]) + 1)
        new_day = int(new_day - 28)
        if 1 < new_day < 10:
            new_day = ''.join('0') + str(new_day)
if month in ('01', '03', '05', '07', '08') and int(new_day) > 31:
    month = ''.join('0') + str(int(list_date[0]) + 1)
    new_day = int(new_day - 31)
    if 1 < new_day < 10:
        new_day = ''.join('0') + str(new_day)
elif month == '10' and new_day > 31:
    month = str(int(list_date[0]) + 1)
    new_day = int(new_day - 31)
    if 1 < new_day < 10:
        new_day = ''.join('0') + str(new_day)
elif month == '12' and new_day > 31:
    month = '01'
    new_day = int(new_day - 31)
    if 1 < new_day < 10:
        new_day = ''.join('0') + str(new_day)
    year = int(year) + 1
elif month in ('04', '06') and new_day > 30:
    month = ''.join('0') + str(int(list_date[0]) + 1)
    new_day = int(new_day - 30)
    if 1 < new_day < 10:
        new_day = ''.join('0') + str(new_day)
elif month in ('09', '11') and new_day > 30:
    month = int(list_date[0]) + 1
    new_day = int(new_day - 30)
    if 1 < new_day < 10:
        new_day = ''.join('0') + str(new_day)
new_date = ''.join(str(month) + '/' + str(new_day) + '/' + str(year))
print(new_date)

"""Input new date into date_field"""
date_field = driver.find_element(By.CSS_SELECTOR, "#datePickerMonthYearInput")
date_field.click()
date_field.send_keys(Keys.BACKSPACE * 10)
time.sleep(5)
date_field.send_keys(new_date)
date_field.send_keys(Keys.RETURN)
print("Input +10 days' date")

"""assertion"""
assert date_field.get_attribute('value') == new_date
print('Date is correct')

time.sleep(3)
driver.close()
