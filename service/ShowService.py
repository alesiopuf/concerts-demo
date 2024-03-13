from domain.validator.ShowValidator import ShowValidator


class ShowService:

    def __init__(self, show_repository, artist_repository):
        self.__show_repository = show_repository
        self.__artist_repository = artist_repository

    def book_show(self, show):
        '''
        Books a show
        :param show: Show to be booked
        :return: The show added and the price
        '''
        ShowValidator.validate_show(show)
        self.__show_repository.add_show(show)
        artist = self.__artist_repository.read_artist_by_id(show.id_artist)
        if show.trupa_live:
            return show, artist.pret + 1000
        return show, artist.pret

    def get_shows(self):
        '''
        Gets all the shows booked
        :return: list with all shows booked
        '''
        return self.__show_repository.read_shows()
