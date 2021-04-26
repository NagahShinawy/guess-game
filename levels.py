"""
created by Nagaj at 25/04/2021
"""
from constants import EASY_TURNS, HARD_TURNS, REMAINING_HARD, REMAINING_EASY, FAILED, SUCCESS


class DifficultyLevel:
    """
    Basic DifficultyLevel
    """

    TURNS = 0
    REMAINING = 0
    RESULT = ""

    def __repr__(self):
        return f"{self.TURNS}"

    def __sub__(self, other):
        return self.REMAINING - other


class EasyLevel(DifficultyLevel):
    """
    implement difficulty easy level
    """

    TURNS = EASY_TURNS
    REMAINING = REMAINING_EASY


class HardLevel(DifficultyLevel):
    """
        implement difficulty hard level
    """

    TURNS = HARD_TURNS
    REMAINING = REMAINING_HARD
