from domain.Artist import Artist
from domain.exception.Exceptions import ConverterException


class ArtistConverter:

    @staticmethod
    def to_artist(string):
        '''
        Converts string to Artist object, raises Exception if not valid
        :param string: string to be converted
        :return: Artist Object
        '''
        try:
            string = string.strip().split(',')
            string = [el.strip() for el in string]
            return Artist(int(string[0]), string[1], string[2], float(string[3]))
        except Exception:
            raise ConverterException(f"Artistul {string} nu a putut fi procesat")

