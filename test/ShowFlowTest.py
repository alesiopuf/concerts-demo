from domain.Show import Show
from repository.ArtistRepository import ArtistRepository
from repository.ShowRepository import ShowRepository
from service.ShowService import ShowService


class ShowFlowTest:
    def __init__(self):
        self.__show_repo = ShowRepository()
        self.__artist_repo = ArtistRepository()
        self.__show_service = ShowService(self.__show_repo, self.__artist_repo)

    def __test_book_show(self):
        assert type(self.__show_service.book_show(Show(1, 1, "Cluj", "10/10/2024", True))[0]) == Show
        assert self.__show_service.book_show(Show(1, 1, "Cluj", "10/10/2024", True))[1] == 1500

    def __test_get_shows(self):
        assert len(self.__show_service.get_shows()) == 0
        self.__show_service.book_show(Show(1, 1, "Cluj", "10/10/2024", True))
        assert len(self.__show_service.get_shows()) == 1

    def run(self):
        self.__test_book_show()
