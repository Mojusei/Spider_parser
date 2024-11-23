from Spider import *
from scripts import write_csv

def main():
    spider = Spider('https://www.mvideo.ru/vse-akcii?from=under_search')
    
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
    
    # Запись в фаил
    write_csv(posts)

    print('Успешно')
    
    # Закрытие браузера
    spider.driver.quit()
    print('Браузер закрыт')


main()