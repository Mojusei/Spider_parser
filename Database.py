import sqlite3


class Database:
    def  __init__(self, db_file):
        self.__db_file = db_file
        self.__connection = self.__create_connection()
        self.__cursor = self.__connection.cursor()
        self.__create_table()

    def __create_connection(self):
        """ Создает соединение с базой данных """

        try:
            conn = sqlite3.connect(self.__db_file)
            return conn
        except sqlite3.Error as e:
            print(e)
        return None

    def __create_table(self):
        """ Создает таблицу posts в базе данных """

        self.__cursor.execute('''
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                refer TEXT NOT NULL
            )
        ''')
        print('Таблица создана')
        self.__connection.commit()

    def insert_data(self, title, refer):
        """ Вставляет данные в таблицу posts """
        
        query = """
        INSERT INTO posts (title, refer)
        SELECT ?, ?
        WHERE NOT EXISTS (
            SELECT 1
            FROM posts
            WHERE title = ? AND refer = ?
            )
        """
        self.__cursor.execute(query, (title, refer, title, refer))
        self.__connection.commit() 

    def get_data(self):
        """ Получает данные из таблицы posts """

        self.__cursor.execute('SELECT * FROM posts')
        return self.__cursor.fetchall()

    def close_db(self):
        self.__connection.close()

