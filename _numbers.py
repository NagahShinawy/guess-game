"""
created by Nagaj at 25/04/2021
"""
import random
from validations import NumberValidation


class BasicNumber:
    """
    basic number implementation
    """
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.value}"

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value


class ComputerNumber(BasicNumber):
    """
    implement computer random number from 1 to 100
    """
    START = 1
    END = 100

    def __init__(self,):
        super().__init__(random.randint(self.START, self.END))


class GuessNumber(BasicNumber):
    """
    implement user guess number
    """

    numbers = []  # all numbers that user try to guess

    def __init__(self, value):
        super().__init__(NumberValidation(value).validate_value)
        self.save()

    def save(self) -> None:
        """
        save single guess number to list of numbers that user is trying with
        :return:
        """
        self.numbers.append(self.value)
