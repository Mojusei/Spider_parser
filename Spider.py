from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class Spider:
    def __init__(self, ref):
        self.ref = ref
        self.__ip = '127.162.186.138'
        self.__port = 80

    def __set_options(self):
        """ Установка опций браузера"""
        
        options = webdriver.FirefoxOptions()
        options.set_preference('dom.webdriver.enabled', False)
        options.set_preference('dom.webnotifications.enabled', False)

        #self.__set_proxy(options)

        return webdriver.Firefox(options=options)
    

    def __set_proxy(self, options):
        """ Установка прокси, пока alpha версия""" 

        options.set_preference('network.proxy.type', 1)
        options.set_preference('network.proxy.http', self.__ip)
        options.set_preference('network.proxy.http_port', self.__port)
        options.set_preference('network.proxy.https', self.__ip)
        options.set_preference('network.proxy.https_port', self.__port)
        options.set_preference('network.proxy.ssl', self.__ip)
        options.set_preference('network.proxy.ssl_port', self.__port)


    def launch_browser(self):
        """ Запуск браузера"""

        try:
            self.driver = self.__set_options()

            self.driver.get(self.ref)
            time.sleep(3)
        except:
            self.driver.quit()
            print('Прокси не работает')


    def get_element(self, xpath):
        """ Получение элемента по Xpath"""

        element = self.driver.find_element(By.XPATH, xpath)
        return element


    def click_element(self, xpath):
        """ Клик по элементу по Xpath"""

        element = self.driver.find_element(By.XPATH, xpath)
        element.click()
        time.sleep(2)


    def input_to_field(self, xpath, text):
        """ Ввод текста в поле по Xpath"""

        input_field = self.driver.find_element(By.XPATH, xpath)
        input_field.send_keys(text)
        input_field.send_keys(Keys.RETURN)
        time.sleep(2)
    

    def change_city(self, city_name):
        """ Изменение города"""

        self.click_element('/html/body/mvid-root/div/mvid-primary-layout/mvid-layout/div/div[1]/mvid-header-container/mvid-header/header/div[1]/div/div[1]/span')
        self.input_to_field('//*[@id="2"]', city_name)

    
    def get_posts_info(self, post_class_name, element_class_name):
        """ Получение информации о постах"""
        from scripts import check_commas
        
        posts = self.driver.find_elements(By.CLASS_NAME, post_class_name) #'o-article-list__item'

        data = []
        for post in posts:
            title = post.find_element(By.CLASS_NAME, element_class_name).find_element(By.TAG_NAME, 'a').text #'c-preview-article__title.height-ready'
            title = check_commas(title)
            refer = post.find_element(By.CLASS_NAME, element_class_name).find_element(By.TAG_NAME, 'a').get_attribute('href')

            data.append({
                'Заголовок' : title,
                'Ссылка' : refer,
            })

        
        data.reverse()

        return data

