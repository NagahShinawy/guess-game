"""
created by Nagaj at 25/04/2021
"""
from constants import NUMBERS_PROMPT, LEVELS_PROMPT
from validations import NumberValidation, LevelValidation


class CMD:
    PROMPT = None

    def __init__(self):
        self.command = self.set_command()

    def set_command(self):
        pass


class CMDNumber(CMD):
    """
        user command line actions
    """

    PROMPT = NUMBERS_PROMPT

    def set_command(self):
        """
        :return:
        """
        number_as_command = input(self.PROMPT)
        while not NumberValidation(number_as_command).validate_value:
            number_as_command = input(self.PROMPT)
        return number_as_command

    @property
    def number_value(self):
        return self.command


class CMDLevel(CMD):
    PROMPT = LEVELS_PROMPT

    def set_command(self):
        """
        :return:
        """
        level_as_command = input(self.PROMPT)
        while not LevelValidation(level_as_command).validate_value:
            level_as_command = input(self.PROMPT)
        return level_as_command

    @property
    def level_value(self):
        return self.command
