from domain.exception.Exceptions import ValidationException


class ShowValidator:

    @staticmethod
    def validate_show(show):
        '''
        Validates show, raises Exception if not valid
        :param show: Show to be validates
        :return: None
        '''
        if show is None:
            raise ValidationException("Showul este NULL!")
