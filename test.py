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
string = 'Покупай сейчас, плати потом'

def check_commas(string):
    """ Проверка на наличие запятых в строке"""
    import re

    res = re.search(',', string)

    if res != None:
        string = string.replace(',', '')
    
    return string


print(check_commas(string))


"""driver.quit()"""
print('Успешно')

