class BaseSBError(Exception):
    # Base StudyBuddyError
    def __init__(self, message):
        super().__init__(message)


class ProcessorError(BaseSBError):
    """Something wrong in processor processes"""