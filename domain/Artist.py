class Artist:

    def __init__(self, id, nume, gen, pret):
        self.__id = id
        self.__nume = nume
        self.__gen = gen
        self.__pret = pret

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def nume(self):
        return self.__nume

    @nume.setter
    def nume(self, value):
        self.__nume = value

    @property
    def gen(self):
        return self.__gen

    @gen.setter
    def gen(self, value):
        self.__gen = value

    @property
    def pret(self):
        return self.__pret

    @pret.setter
    def pret(self, value):
        self.__pret = value

    def __str__(self):
        return f'ARTIST({self.__id}, {self.__nume}, {self.__gen}, {self.__pret})'

    def __repr__(self):
        return str(self)
