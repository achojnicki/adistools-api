#args check
class ArgsCheckException(Exception):
    pass

class MissingField(ArgsCheckException):
    pass

#auth
class AuthException(Exception):
    pass

class UserDoNotExist(AuthException):
    pass

class PasswordDoNotMatch(AuthException):
    pass

#url shortener
class URLShortenerException(Exception):
    pass

class RedirectionQueryExists(URLShortenerException):
    pass


