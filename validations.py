"""
created by Nagaj at 25/04/2021
"""
from constants import INVALID_NUMBER, INVALID_LEVEL, VALID_LEVELS


class BasicValidation:
    """
    Basic Validation
    """

    def __init__(self, value):
        self.value = value

    @property
    def validate_value(self):
        """
        basic validation for number, level, ....
        :return: validated number
        """
        return self.value


class NumberValidation(BasicValidation):
    """
    Validation for number used by user [ between 1 to 100]
    """

    START = 1
    END = 100

    @property
    def validate_value(self):
        """
        validate user number from 1 to 100
        :return: validated command number
        """
        number_error = INVALID_NUMBER.format(
            number=self.value, start=self.START, end=self.END
        )
        try:
            self.value = int(self.value)
        except ValueError:
            print(number_error)
            return False
        if self.value not in range(self.START, self.END + 1):
            print(number_error)
            return False
        return self.value


class LevelValidation(BasicValidation):
    """
       Validation for level. Must be one of 'easy' or 'hard' [case insensitive]
    """

    LEVELS = VALID_LEVELS

    @property
    def validate_value(self):
        """
        validation for level
        :return: validated level 'easy' or 'hard'
        """
        value = self.value.lower()
        if value not in self.LEVELS:
            print(INVALID_LEVEL.format(level=self.value))
            return False
        return value
