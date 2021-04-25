"""
created by Nagaj at 25/04/2021
"""
from constants import EASY_TURNS, HARD_TURNS


class DifficultyLevel:
    """
    Basic DifficultyLevel
    """
    TURNS = 0


class EasyLevel(DifficultyLevel):
    """
    implement difficulty easy level
    """
    TURNS = EASY_TURNS


class HardLevel(DifficultyLevel):
    """
        implement difficulty hard level
    """
    TURNS = HARD_TURNS
