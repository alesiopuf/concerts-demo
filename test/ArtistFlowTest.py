from repository.ArtistRepository import ArtistRepository
from service.ArtistService import ArtistService


class ArtistFlowTest:

    def __init__(self):
        self.__artist_repo = ArtistRepository()
        self.__artist_service = ArtistService(self.__artist_repo)

    def __test_get_artists_with_higher_price(self):
        assert len(self.__artist_service.get_artists_with_higher_price(1000)) == 3
        assert len(self.__artist_service.get_artists_with_higher_price(100)) == 9

    def run(self):
        self.__test_get_artists_with_higher_price()
