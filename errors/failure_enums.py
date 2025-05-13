from exqt_error import ExqtError

# todo: refining error message & code

FailureIncompleteInitiation = ExqtError("", -1)

FailureHttpRequest = ExqtError("", 4)

FailureMissingMedia = ExqtError("", 5)

FailureEmptyInput = ExqtError("", 6)

FailureInvalidInput = ExqtError("", 8)

FailureMalformMedia = ExqtError("", 9)
