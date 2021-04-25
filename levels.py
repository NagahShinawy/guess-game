"""
created by Nagaj at 25/04/2021
"""
from constants import EASY_TURNS, HARD_TURNS


class DifficultyLevel:
    TURNS = 0


class EasyLevel(DifficultyLevel):
    TURNS = EASY_TURNS


class HardLevel(DifficultyLevel):
    TURNS = HARD_TURNS
