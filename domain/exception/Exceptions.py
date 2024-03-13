class ConverterException(Exception):
    def __init__(self, msg):
        Exception.__init__(self)
        self.__msg = msg

    @property
    def msg(self):
        return self.__msg

    @msg.setter
    def msg(self, value):
        self.__msg = value


class ValidationException(Exception):
    def __init__(self, msg):
        Exception.__init__(self)
        self.__msg = msg

    @property
    def msg(self):
        return self.__msg

    @msg.setter
    def msg(self, value):
        self.__msg = value
