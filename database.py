import psycopg2 as ps


class DataBase:
    def __init__(self, user, password, name, host='localhost'):
        self.user = user
        self.password = password
        self.name = name
        self.host = host

        con = ps.connect(
            user=user,
            password=password,
            database='postgres',
            host=host
        )
        
        con.autocommit = True
        cur = con.cursor()
        cur.execute("SELECT datname FROM pg_database;")

        if (name,) not in cur.fetchall():
            cur.execute(f"CREATE DATABASE {name};")
        con.close()
        cur.close()

        self.connection = ps.connect(
            user=user,
            password=password,
            database=name,
            host=host
        )
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        self.cursor.execute(open('init.sql', 'r').read())
        self.init_tables()
        self.cursor.execute(open('functions.sql', 'r').read())

    def drop_database(self):
        self.connection = ps.connect(
            user=self.user,
            password=self.password,
            database='postgres',
            host=self.host
        )
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"DROP DATABASE {self.name}")
    
    def init_tables(self):
        self.cursor.callproc("init_tables")

    # GAMES ---------------------------------------------------------
    def add_game(self, name, genre, version):
        self.cursor.callproc("add_game", (name, genre, version,))

    def delete_game(self, name):
        self.cursor.callproc("delete_game", (name, ))

    def get_games(self):
        self.cursor.callproc("get_games")
        return self.cursor.fetchone()[0]

    def delete_games(self):
        self.cursor.callproc("delete_games")
    
    def find_games_by_genre(self, genre):
        self.cursor.callproc("find_games_by_genre", (genre,))
        return self.cursor.fetchone()[0]

    def delete_games_by_genre(self, genre):
        self.cursor.callproc("delete_games_by_genre", (genre,))

    def update_game_version(self, newver, name):
        self.cursor.callproc("update_game_version", (newver, name,))
    
    # -------------------------------------------------------------

    # PUBLISHERS ---------------------------------------------------------
    def add_publisher(self, name, country, f_date):
        self.cursor.callproc("add_publisher", (name, country, f_date,))

    def delete_publisher(self, name):
        self.cursor.callproc("delete_publisher", (name, ))

    def get_publishers(self):
        self.cursor.callproc("get_publishers")
        return self.cursor.fetchone()[0]

    def delete_publishers(self):
        self.cursor.callproc("delete_publishers")
    
    def find_publishers_by_country(self, country):
        self.cursor.callproc("find_publishers_by_country", (country,))
        return self.cursor.fetchone()[0]

    def delete_publishers_by_country(self, country):
        self.cursor.callproc("delete_publishers_by_genre", (country,))

    def update_publisher_name(self, new, name):
        self.cursor.callproc("update_publisher_name", (new, name,))
    # -------------------------------------------------------------

    # CREATORS ---------------------------------------------------------
    def add_creator(self, name, country, email):
        self.cursor.callproc("add_creator", (name, country, email,))

    def delete_creator(self, name):
        self.cursor.callproc("delete_creator", (name, ))

    def get_creators(self):
        self.cursor.callproc("get_creators")
        return self.cursor.fetchone()[0]

    def delete_creators(self):
        self.cursor.callproc("delete_creators")
    
    def find_creators_by_country(self, country):
        self.cursor.callproc("find_creators_by_country", (country,))
        return self.cursor.fetchone()[0]

    def delete_creators_by_country(self, country):
        self.cursor.callproc("delete_creators_by_country", (country,))

    def update_creator_name(self, new, name):
        self.cursor.callproc("update_creator_name", (new, name,))
    # -------------------------------------------------------------

    # PUBLICATIONS ---------------------------------------------------------
    def add_publication(self, g_name, p_name, c_name, date, platform):
        self.cursor.callproc("add_publication", (g_name, p_name, c_name, date, platform,))

    def delete_publication(self, id):
        self.cursor.callproc("delete_publication", (id, ))

    def get_publications(self):
        self.cursor.callproc("get_publications")
        return self.cursor.fetchone()[0]

    def delete_publications(self):
        self.cursor.callproc("delete_publications")

    def update_publication_platform(self, new, id):
        self.cursor.callproc("update_publication_platform", (new, id,))
    # -------------------------------------------------------------