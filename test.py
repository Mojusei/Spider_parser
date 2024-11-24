from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time
import csv
import re


"""options = webdriver.FirefoxOptions()
options.set_preference('dom.webdriver.enabled', False)
options.set_preference('dom.webnotifications.enabled', False)

driver = webdriver.Firefox(options=options)

ref = 'https://www.mvideo.ru/vse-akcii'

driver.get(ref)
time.sleep(3)"""
with open('stocks.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        print(f"{row['Заголовок']}: {row['Ссылка']}\n\n")




"""driver.quit()"""
print('Успешно')

