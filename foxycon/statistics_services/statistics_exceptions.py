class ParsingNotPossible(Exception):
    """
    The base class for inability to start parsing social media exceptions
    """

    def __init__(self, message: str) -> None:
        super().__init__(message)


class RequiredTelegramAccount(ParsingNotPossible):
    """
    To parse telegram, you need to add at least one account
    """

    def __init__(self) -> None:
        message = (
            "To parse telegram, you need to add at least one account"
        )
        super().__init__(message)