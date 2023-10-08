class ArgsCheckException(Exception):
    pass

class MissingField(ArgsCheckException):
    pass


class URLShortenerException(Exception):
    pass

class RedirectionQueryExists(URLShortenerException):
    pass
