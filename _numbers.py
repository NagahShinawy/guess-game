"""
created by Nagaj at 25/04/2021
"""
import random
from validations import NumberValidation


class BasicNumber:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.value}"

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value


class ComputerNumber(BasicNumber):
    START = 1
    END = 100

    def __init__(self,):
        super().__init__(random.randint(self.START, self.END))


class GuessNumber(BasicNumber):
    def __init__(self, value):
        super().__init__(NumberValidation(value).validate_value)
