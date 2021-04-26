"""
created by Nagaj at 25/04/2021
"""

import datetime
import json
import os

from constants import DATETIME_FORMAT

turnspath = os.path.join(os.getcwd(), "turns.json")


def create_turn(
    computer_number: int, guess_numbers: list, turns: int, result: str
) -> dict:
    now = datetime.datetime.now()
    return {
        "computer_number": computer_number,
        "guess_numbers": guess_numbers,
        "turns": turns,
        "result": result,
        "datetime": datetime.datetime.strftime(now, DATETIME_FORMAT),
    }


def load() -> list:
    with open(turnspath, "r") as turns_file:
        turns = json.load(turns_file)

    return turns


def save(turn: dict):
    turns = load()
    turns.append(turn)
    with open(turnspath, "w") as turns_file:
        json.dump(turns[::-1], turns_file, indent=4)
