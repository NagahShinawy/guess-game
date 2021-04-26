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
        """
        basic method for set commands
        :return:
        """
        return f"<{self}>"

    def __repr__(self):
        return self.command

    def __eq__(self, other):
        """
        compare value entered by user with excepted value
        in case of number should be in range 1 to 100.
        in case of level should be on of 'easy' or 'hard'
        :param other: validated value entered by the user
        :return: True if validated value (1 to 100) or (easy or hard)
        """
        return self.command == other

    @property
    def get_value(self):
        """

        :return: get value entered by the user
        """
        return self.command


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
