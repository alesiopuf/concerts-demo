from domain.converter.ArtistConverter import ArtistConverter


class ArtistRepository:

    def __init__(self):
        self.__filename = 'artisti.txt'

    def read_artists(self):
        '''
        Reads all artists from file
        :return: list with all artists in file
        '''
        with open(self.__filename, 'r') as file:
            artists = file.readlines()
            artists = [ArtistConverter.to_artist(element) for element in artists]
            return artists

    def read_artist_by_id(self, artist_id):
        '''
        Reads artist by id
        :param artist_id: id of artist to be found
        :return: artist object
        '''
        with open(self.__filename, 'r') as file:
            artists = file.readlines()
            artists = [ArtistConverter.to_artist(element) for element in artists]
            for artist in artists:
                if artist.id == artist_id:
                    return artist
