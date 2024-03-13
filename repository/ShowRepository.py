class ShowRepository:

    def __init__(self):
        self.__shows = []

    def add_show(self, show):
        '''
        Add a show to the memory
        :param show: Show to be booked
        :return: Show that was saved
        '''
        self.__shows.append(show)
        return show

    def read_shows(self):
        '''
        Reads all shows booked stored in memory
        :return: list with all shows
        '''
        return self.__shows
