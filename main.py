"""
created by Nagaj at 25/04/2021
"""
from cmd import CMDNumber, CMDLevel
from _numbers import ComputerNumber, GuessNumber
from levels import EasyLevel, HardLevel
from utils import help_msg
from constants import (
    REMAINING_TURNS_MSG,
    EASY,
    DONE,
    MIN_REMAINING_TURNS,
    REMAINING_EASY,
    REMAINING_HARD,
)


def main():
    level_as_command = CMDLevel()
    number_as_command = CMDNumber()

    # ##########################################

    guessnumber = GuessNumber(number_as_command.number_value)
    computernumber = ComputerNumber()

    # ##########################################

    if level_as_command.level_value == EASY:
        level = EasyLevel()
        remaining = REMAINING_EASY
    else:
        level = HardLevel()
        remaining = REMAINING_HARD

    turns = level.TURNS
    # print(computernumber)
    # ##########################################

    while (guessnumber != computernumber) and (turns > MIN_REMAINING_TURNS):
        turns -= 1
        help_msg(computernumber=computernumber, guessnumber=guessnumber)
        print(REMAINING_TURNS_MSG.format(turns=turns))
        number_as_command = CMDNumber()
        guessnumber = GuessNumber(number_as_command.number_value)

    if turns >= 0:
        print(DONE.format(turns=remaining - turns))

    # ##########################################


if __name__ == "__main__":
    main()
