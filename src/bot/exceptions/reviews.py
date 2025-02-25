class NotAllValuesPassed(Exception):
    """Exception is called when not all values were passed to API."""

    pass


class ReviewAlreadyExists(Exception):
    """Exception is called when user have already reviewed a certain movie."""

    pass
