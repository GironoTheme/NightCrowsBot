import mysql.connector


class Database:
    """Класс для работы с базой данных"""

    def __init__(self):
        self.host = '127.0.0.1'
        self.user = 'root'
        self.password = 'root'
        self.name_of_base = 'albion_items'

        self.config = {
            'user': self.user,
            'password': self.password,
            'host': self.host,
        }

        self.connection = mysql.connector.connect(**self.config)
        self.cursor = self.connection.cursor()

        # Создаем базу данных, если она отсутствует
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.name_of_base}")
        self.config['database'] = self.name_of_base  # Обновляем конфиг с указанием новой базы данных
        self.connection.close()  # Закрываем старое соединение

        # Обновляем соединение и курсор с новым именем базы данных
        self.connection = mysql.connector.connect(**self.config)
        self.cursor = self.connection.cursor()

    def make_query(self, query):
        """Функция для того чтобы сделать прямой запрос к базе данных"""
        self.cursor.execute(query)
        return self.cursor.fetchall()


#db = Database()

#db.make_query("CREATE TABLE purchase_and_sale(product_id INT PRIMARY KEY, character_id INT, product_name varchar(50), purchase_price FLOAT, sale_price FLOAT, ratio INT, count INT, FOREIGN KEY (character_id) REFERENCES characters(character_id))")

#db.make_query("ALTER TABLE characters RENAME COLUMN characters_id TO character_id")
#db.make_query("CREATE TABLE characters (character_id INT PRIMARY KEY AUTO_INCREMENT, character_name varchar(255), position INT, FOREIGN KEY (position) REFERENCES cords_for_characters(cords_id));")

#db.make_query("CREATE TABLE character_server (character_id INT, server_id INT, PRIMARY KEY (character_id, server_id),FOREIGN KEY (character_id) REFERENCES characters(character_id),FOREIGN KEY (server_id) REFERENCES servers(server_id));")

#db.make_query("create table servers (server_id INT PRIMARY KEY AUTO_INCREMENT, server_name varchar(255), position_x INT, position_y INT);")

#db.make_query("CREATE TABLE cords_for_characters (cords_id INT PRIMARY KEY AUTO_INCREMENT, position_x INT, position_y INT);")

#db.make_query("ALTER TABLE characters ADD email VARCHAR(50)")

#db.make_query("INSERT INTO characters (character_name, position)"
#              "VALUES ('TheSempay', 1);")

#db.make_query("INSERT INTO character_server (character_id, server_id)"
#              "VALUES (7, 5);")
#print(db.make_query("SELECT servers.name_server, servers.position_x, servers.position_y, characters.position_x, characters.position_y FROM servers JOIN character_server ON servers.server_id = character_server.server_id JOIN characters ON character_server.character_id = characters.character_id;"))

#print(db.make_query("select * from servers"))
#db.make_query("DELETE FROM servers")
#db.make_query("INSERT INTO servers (server_name, position_x, position_y )"
#              "VALUES ('UE Central', 200, 570);")

#AP Southeast": {"cords": [200, 380], "characters": [[200, 540]]},
#  "SA East": {"cords": [200, 440], "characters": [[200, 440]]},
#  "US West": {"cords": [200, 580], "characters": [[200, 440]]},
#  "US East": {"cords": [200, 540], "characters": [[200, 640], [200, 540], [200, 440]]},
#  "UE Central": {"cords": [200, 580], "characters": [[200, 440]]}


#f"ALTER TABLE {tab} MODIFY product_id INT AUTO_INCREMENT"
