class Show:

    def __init__(self, id, id_artist, locatie, data, trupa_live):
        self.__id = id
        self.__id_artist = id_artist
        self.__locatie = locatie
        self.__data = data
        self.__trupa_live = trupa_live

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def id_artist(self):
        return self.__id_artist

    @id_artist.setter
    def id_artist(self, value):
        self.__id_artist = value

    @property
    def locatie(self):
        return self.__locatie

    @locatie.setter
    def locatie(self, value):
        self.__locatie = value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def trupa_live(self):
        return self.__trupa_live

    @trupa_live.setter
    def trupa_live(self, value):
        self.__trupa_live = value

    def __str__(self):
        return f'SPECTACOL({self.__id}, {self.id_artist}, {self.__locatie}, {self.__data}, {self.__trupa_live})'

    def __repr__(self):
        return str(self)
    