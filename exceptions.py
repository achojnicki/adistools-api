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

#logs
class LogsException(Exception):
    pass

class LogsProjectExists(LogsException):
    pass


#args_validator
class FormValidatorException(Exception):
    pass

class FormDefinitionSyntaxError(FormValidatorException):
    pass

class ValidationError(FormValidatorException):
    pass

class FormNotDefined(FormValidatorException):
    pass