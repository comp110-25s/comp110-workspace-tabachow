"""File to define Fish class."""


class Fish:
    """Fish class."""

    age: int

    def __init__(self):
        """Fish class initialization."""
        self.age = 0
        return None

    def one_day(self):
        """Increases the value of the age attribute by 1."""
        self.age += 1
        return None
