class MissingLabelError(KeyError):
    pass


class PageNotFoundError(LookupError):
    pass


class IncorrectPasswordError(ValueError):
    pass


class IncorrectUsernameError(ValueError):
    pass


class APIThrottleLimitError(RuntimeError):
    pass


try:
    login()
except IncorrectUsernameError:
    print("your username was incorrect!")
except IncorrectPasswordError:
    print("your password was incorrect")
