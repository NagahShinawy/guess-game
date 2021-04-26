"""
created by Nagaj at 25/04/2021
"""
from constants import NUMBERS_PROMPT, LEVELS_PROMPT
from validations import NumberValidation, LevelValidation


class CMD:
    """
    Basic CMD to handle  CLI
    """

    PROMPT = None

    def __init__(self):
        self.command = self.set_command()

    def set_command(self):
        pass


class CMDNumber(CMD):
    """
        user number CLI
    """

    PROMPT = NUMBERS_PROMPT

    def set_command(self):
        """
        Validate number command . Must be in range 1 to 100
        :return: validated command number. number between 1 to 100
        """
        number_as_command = input(self.PROMPT)
        while not NumberValidation(number_as_command).validate_value:
            number_as_command = input(self.PROMPT)
        return number_as_command

    @property
    def number_value(self):
        return self.command


class CMDLevel(CMD):
    """
    user level CLI
    """

    PROMPT = LEVELS_PROMPT

    def set_command(self):
        """
        Validate level command . Must be one of 'easy' or 'hard'. [case insensitive]
        :return: validated command level 'easy' or 'hard'
        """
        level_as_command = input(self.PROMPT)
        while not LevelValidation(level_as_command).validate_value:
            level_as_command = input(self.PROMPT)
        return level_as_command

    @property
    def level_value(self):
        """

        :return: level command value 'easy' or 'hard'
        """
        return self.command

    def __eq__(self, other):
        """

        :param other: one of 'easy' or 'hard'
        :return: True if command = easy else False
        """
        return self.command == other
