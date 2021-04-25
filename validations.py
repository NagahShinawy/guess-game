"""
created by Nagaj at 25/04/2021
"""
from constants import INVALID_NUMBER, INVALID_LEVEL


class BasicValidation:

    def __init__(self, value):
        self.value = value

    @property
    def validate_value(self):
        return self.value


class NumberValidation(BasicValidation):
    START = 1
    END = 100

    @property
    def validate_value(self):
        if self.value not in range(self.START, self.END + 1):
            raise ValueError(INVALID_NUMBER.format(number=self.value, start=self.START, end=self.END))
        return self.value


class LevelValidation(BasicValidation):
    LEVELS = ("easy", "hard")

    @property
    def validate_value(self):
        value = self.value.lower()
        if value not in self.LEVELS:
            raise ValueError(INVALID_LEVEL.format(level=self.value))
        return value
