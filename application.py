from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem
from database import DataBase

import connectWindow
import mainWindow

class ConnectWindow(QtWidgets.QMainWindow, connectWindow.Ui_ConnectWindow):
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)

        self.app = app
        self.connectButton.clicked.connect(self.connect_to)

    def connect_to(self):
        self.app.connect_to_database(self.userText.text(), self.passwordText.text(), self.databaseText.text())
        self.close()

class MainWindow(QtWidgets.QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self,):
        super().__init__()
        self.setupUi(self)

        self.db = None
        self.changed = False
        self.cur_tab = 'Разработчики'
        self.connectWindow = ConnectWindow(self)
        self.columns_creators = ['name', 'country', 'email']
        self.columns_publishers = ['name', 'country', 'foundation_date']
        self.columns_games = ['name', 'genre', 'version']
        self.columns_publications = ['id', 'game_name', 'publisher_name', 'creator_name', 'date', 'platform']

        # Toolbar
        self.connectAction.triggered.connect(self.connectWindow.show)
        self.tabWidget.tabBarClicked.connect(self.get_current_tab)
        self.clearAction.triggered.connect(self.clear_current)
        self.clearAllAction.triggered.connect(self.clear_all)
        self.dropAction.triggered.connect(self.drop_database)

        # Creators
        self.creatorsTable.setColumnCount(len(self.columns_creators))
        self.creatorsTable.setHorizontalHeaderLabels(self.columns_creators)
        self.creatorsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.addCreatorsButton.clicked.connect(self.add_creator)
        self.deleteCreatorsButton.clicked.connect(self.delete_creator)
        self.searchCreatorsButton.clicked.connect(self.search_creators)
        self.deleteSearchCreatorsButton.clicked.connect(self.delete_search_creators)
        self.creatorsTable.itemChanged.connect(self.update_creators)
        
        # Publishers
        self.publishersTable.setColumnCount(len(self.columns_publishers))
        self.publishersTable.setHorizontalHeaderLabels(self.columns_publishers)
        self.publishersTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.addPublishersButton.clicked.connect(self.add_publisher)
        self.deletePublishersButton.clicked.connect(self.delete_publisher)
        self.searchPublishersButton.clicked.connect(self.search_publishers)
        self.deleteSearchPublishersButton.clicked.connect(self.delete_search_publishers)
        self.publishersTable.itemChanged.connect(self.update_publishers)

        # Games
        self.gamesTable.setColumnCount(len(self.columns_games))
        self.gamesTable.setHorizontalHeaderLabels(self.columns_games)
        self.gamesTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.addGamesButton.clicked.connect(self.add_game)
        self.deleteGamesButton.clicked.connect(self.delete_game)
        self.searchGamesButton.clicked.connect(self.search_games)
        self.deleteSearchGamesButton.clicked.connect(self.delete_search_games)
        self.gamesTable.itemChanged.connect(self.update_games)

        # Publications
        self.publicationsTable.setColumnCount(len(self.columns_publications))
        self.publicationsTable.setHorizontalHeaderLabels(self.columns_publications)
        self.publicationsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.addPublicationsButton.clicked.connect(self.add_publication)
        self.deletePublicationsButton.clicked.connect(self.delete_publication)

    def delete_publication(self):
        if len(self.publicationsTable.selectedIndexes()):
            for i in self.publicationsTable.selectedIndexes():
                self.db.delete_publication(self.publications[i.row()]['name'])
                self.publications = self.db.get_publications()
                self.set_data(self.publicationsTable, self.columns_publications, self.publications)

    def add_publication(self):
        self.db.add_publication(
            g_name=self.gamePublicationsText.text(),
            p_name=self.publisherPublicationsText.text(),
            c_name=self.creatorPublicationText.text(),
            date=self.datePublicationsText.text(),
            platform=self.platformPublicationsText.text()
        )
        self.publications = self.db.get_publications()
        self.set_data(self.publicationsTable, self.columns_publications, self.publications)
        self.gamePublicationsText.clear()
        self.publisherPublicationsText.clear()
        self.creatorPublicationText.clear()
        self.datePublicationsText.clear()
        self.platformPublicationsText.clear()

    def update_games(self, item):
        if not self.changed:
            self.db.update_game_version(float(item.text()), self.games[item.row()]['name'])
            self.games = self.db.get_games()
            self.set_data(self.gamesTable, self.columns_games, self.games)
            self.publications = self.db.get_publications()
            self.set_data(self.publicationsTable, self.columns_publications, self.publications)

    def delete_search_games(self):
        self.db.delete_games_by_genre(self.genreSearchGamesText.text())
        self.games = self.db.get_games()
        self.set_data(self.gamesTable, self.columns_games, self.games)

    def search_games(self):
        if self.genreSearchGamesText.text() == '':
            self.games = self.db.get_games()
        else:
            self.games = self.db.find_games_by_genre(self.genreSearchGamesText.text())
        self.set_data(self.gamesTable, self.columns_games, self.games)

    def delete_game(self):
        if len(self.gamesTable.selectedIndexes()):
            for i in self.gamesTable.selectedIndexes():
                self.db.delete_game(self.games[i.row()]['name'])
                self.games = self.db.get_games()
                self.set_data(self.gamesTable, self.columns_games, self.games)

    def add_game(self):
        self.db.add_game(
            name=self.nameGamesText.text(),
            genre=self.genreGamesText.text(),
            version=float(self.versionGamesText.text())
        )
        self.games = self.db.get_games()
        self.set_data(self.gamesTable, self.columns_games, self.games)
        self.nameGamesText.clear()
        self.genreGamesText.clear()
        self.versionGamesText.clear()

    def update_publishers(self, item):
        if not self.changed:
            self.db.update_publisher_name(item.text(), self.publishers[item.row()]['name'])
            self.publishers = self.db.get_publishers()
            self.set_data(self.publishersTable, self.columns_publishers, self.publishers)
            self.publications = self.db.get_publications()
            self.set_data(self.publicationsTable, self.columns_publications, self.publications)

    def delete_search_publishers(self):
        self.db.delete_publishers_by_country(self.countrySearchPublishersText.text())
        self.publishers = self.db.get_publishers()
        self.set_data(self.publishersTable, self.columns_publishers, self.publishers)
    
    def search_publishers(self):
        if self.countrySearchPublishersText.text() == '':
            self.publishers = self.db.get_publishers()
        else:
            self.publishers = self.db.find_publishers_by_country(self.countrySearchPublishersText.text())
        self.set_data(self.publishersTable, self.columns_publishers, self.publishers)

    def delete_publisher(self):
        if len(self.publishersTable.selectedIndexes()):
            for i in self.publishersTable.selectedIndexes():
                self.db.delete_publisher(self.publishers[i.row()]['name'])
                self.publishers = self.db.get_publishers()
                self.set_data(self.publishersTable, self.columns_publishers, self.publishers)

    def add_publisher(self):
        self.db.add_publisher(
            name=self.namePublishersText.text(),
            country=self.countryPublishersText.text(),
            f_date=self.datePublishersText.text()
        )
        self.publishers = self.db.get_publishers()
        self.set_data(self.publishersTable, self.columns_publishers, self.publishers)
        self.namePublishersText.clear()
        self.countryPublishersText.clear()
        self.datePublishersText.clear()

    def update_creators(self, item):
        if not self.changed:
            self.db.update_creator_name(item.text(), self.creators[item.row()]['name'])
            self.creators = self.db.get_creators()
            self.set_data(self.creatorsTable, self.columns_creators, self.creators)
            self.publications = self.db.get_publications()
            self.set_data(self.publicationsTable, self.columns_publications, self.publications)

    def drop_database(self):
        self.db.drop_database()
        self.connectWindow.show()

    def clear_all(self):
        self.db.delete_creators()
        self.creators = self.db.get_creators()
        self.set_data(self.creatorsTable, self.columns_creators, self.creators)

        self.db.delete_publishers()
        self.publishers = self.db.get_publishers()
        self.set_data(self.publishersTable, self.columns_publishers, self.publishers)

        self.db.delete_games()
        self.games = self.db.get_games()
        self.set_data(self.gamesTable, self.columns_games, self.games)

        self.db.delete_publications()
        self.publications = self.db.get_publications()
        self.set_data(self.publicationsTable, self.columns_publications, self.publications)

    def clear_current(self):
        if self.cur_tab == 'Разработчики':
            self.db.delete_creators()
            self.creators = self.db.get_creators()
            self.set_data(self.creatorsTable, self.columns_creators, self.creators)
        elif self.cur_tab == 'Издатели':
            self.db.delete_publishers()
            self.publishers = self.db.get_publishers()
            self.set_data(self.publishersTable, self.columns_publishers, self.publishers)
        elif self.cur_tab == 'Игры':
            self.db.delete_games()
            self.games = self.db.get_games()
            self.set_data(self.gamesTable, self.columns_games, self.games)
        elif self.cur_tab == 'Публикации':
            self.db.delete_publications()
            self.publications = self.db.get_publications()
            self.set_data(self.publicationsTable, self.columns_publications, self.publications)

    def get_current_tab(self, index):
        self.cur_tab = ['Публикации', 'Игры', 'Издатели', 'Разработчики'][index]

    def delete_search_creators(self):
        self.db.delete_creators_by_country(self.countrySearchCreatorsText.text())
        self.creators = self.db.get_creators()
        self.set_data(self.creatorsTable, self.columns_creators, self.creators)

    def search_creators(self):
        if self.countrySearchCreatorsText.text() == '':
            self.creators = self.db.get_creators()
        else:
            self.creators = self.db.find_creators_by_country(self.countrySearchCreatorsText.text())
        self.set_data(self.creatorsTable, self.columns_creators, self.creators)
        
    def delete_creator(self):
        if len(self.creatorsTable.selectedIndexes()):
            for i in self.creatorsTable.selectedIndexes():
                self.db.delete_creator(self.creators[i.row()]['name'])
                self.creators = self.db.get_creators()
                self.set_data(self.creatorsTable, self.columns_creators, self.creators)

    def add_creator(self):
        self.db.add_creator(
            name=self.nameCreatorsText.text(),
            country=self.countryCreatorsText.text(),
            email=self.emailCreatorsText.text()
        )
        self.creators = self.db.get_creators()
        self.set_data(self.creatorsTable, self.columns_creators, self.creators)
        self.nameCreatorsText.clear()
        self.countryCreatorsText.clear()
        self.emailCreatorsText.clear()

    def connect_to_database(self, user, pswd, name, host='localhost'):
        self.db = DataBase(
            user=user,
            password=pswd,
            name=name,
            host=host
        )
        self.games = self.db.get_games()
        self.publishers = self.db.get_publishers()
        self.creators = self.db.get_creators()
        self.publications = self.db.get_publications()
        self.set_data(self.gamesTable, self.columns_games, self.games)
        self.set_data(self.publishersTable, self.columns_publishers, self.publishers)
        self.set_data(self.publicationsTable, self.columns_publications, self.publications)
        self.set_data(self.creatorsTable, self.columns_creators, self.creators)

    def set_data(self, table, columns, data):
        self.changed = True
        if data is not None:
            table.setRowCount(len(data))
            for i, row in enumerate(data):
                for j, col in enumerate(columns):
                    table.setItem(i, j, QTableWidgetItem(str(row[col])))
        else:
            table.setRowCount(0)
        self.changed = False
