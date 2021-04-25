"""
created by Nagaj at 25/04/2021
"""
from constants import NUMBERS_PROMPT
from numbers import NumberValidation


class CMD:
    """
        user command line actions
    """

    NUMBERS_PROMPT = NUMBERS_PROMPT

    def __init__(self):
        self.number_as_command = self.set_command()

    def set_command(self):
        """
        :return:
        """
        number_as_command = input(self.NUMBERS_PROMPT)
        while not NumberValidation(number_as_command).validate_value:
            number_as_command = input(self.NUMBERS_PROMPT)
        return number_as_command

    @property
    def number_value(self):
        return self.number_as_command
