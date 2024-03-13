class ArtistService:

    def __init__(self, artist_repository):
        self.__artist_repository = artist_repository

    def get_artists_with_higher_price(self, pret_dorit):
        '''
        Filters artists with higher price than input price
        :param pret_dorit: input price
        :return: list of artists with higher price
        '''
        artists = self.__artist_repository.read_artists()
        filtered = []
        for artist in artists:
            if artist.pret > pret_dorit:
                filtered.append(artist)
        return filtered
