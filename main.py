from Spider import *
from scripts import write_csv, update_db_data

def main():
    spider = Spider('https://www.mvideo.ru/vse-akcii?from=under_search')
    
    try:
        # Запуск браузера
        spider.launch_browser()
        print('Браузер запущен')


        # Изменение города
        # Будет прекрасно работать при отсутствии защиты!
        """
        city = spider.get_element('/html/body/div[2]/div/div[1]/div[3]/div[1]/div/a[1]/span').text
        if city != 'Астрахань':
            spider.change_city('Астрахань')
        """

        # Получение информации о постах с акциями
        posts = spider.get_posts_info('o-article-list__item', 'c-preview-article__title.height-ready')
        
        print("Парсинг завершен\n",
            f"Всего постов: {len(posts)}\n")
        
        # Запись в кэш csv
        write_csv(posts)

        print('Успешно')
        
        # Закрытие браузера
        spider.driver.quit()
        print('Браузер закрыт')
    except:
        spider.driver.quit()
        print('Не удалось получить данные. Ошибка соединения')

    finally:
        # Обновление базы данных из кэша csv
        update_db_data()


main()