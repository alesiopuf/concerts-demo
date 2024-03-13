from domain.exception.Exceptions import ConverterException
from domain.Show import Show


class ShowConverter:

    @staticmethod
    def to_show(string):
        '''
        Converts string to Show object, raises Exception if not valid
        :param string: string to be converted
        :return: Show Object
        '''
        try:
            string = string.strip().split(',')
            string = [el.strip() for el in string]
            trupa_live = True
            if string[4] == "da":
                trupa_live = True
            elif string[4] == "nu":
                trupa_live = False
            else:
                raise ConverterException("Trupa Live trebuie specificata prin da sau nu")
            return Show(int(string[0]), int(string[1]), string[2], string[3], trupa_live)
        except Exception:
            raise ConverterException(f"Spectacolul {string} nu a putut fi procesat")
