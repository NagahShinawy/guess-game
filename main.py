"""
created by Nagaj at 25/04/2021
"""
from cmd import CMDNumber, CMDLevel
from _numbers import ComputerNumber, GuessNumber
from constants import (
    REMAINING_TURNS_MSG,
    EASY,
    DONE_MSG,
    FAILED_MSG,
    MIN_REMAINING_TURNS,
)
from levels import EasyLevel, HardLevel
from results import FailedResult, SuccessResult
from turns import create_turn, save
from utils import help_msg


def check_level(level_as_command):
    """
    check level if easy or hard
    :param level_as_command:
    :return: level
    """
    if level_as_command == EASY:
        level = EasyLevel()
    else:
        level = HardLevel()
    return level


def check_result(turns, level) -> str:
    """
    check result 'failed' or 'success'
    :param turns:  based on tries, we can know the result. turns > 0 means success else failed
    :param level: level that we are working on (easy, hard).
    :return: 'success' or 'failed'
    """
    if turns < MIN_REMAINING_TURNS:
        print(FAILED_MSG.format(level.TURNS))
        result = FailedResult()
    else:
        print(DONE_MSG.format(turns=level - turns))
        result = SuccessResult()
    return result.TEXT


def main():
    """
    entry point for program
    :return:
    """
    computernumber = ComputerNumber()
    print(computernumber)
    level_as_command = CMDLevel()
    number_as_command = CMDNumber()

    # ##########################################

    guessnumber = GuessNumber(number_as_command.get_value)

    # ##########################################

    level = check_level(level_as_command)
    turns = level.TURNS

    # ##########################################

    while guessnumber != computernumber:
        turns -= 1
        if turns < MIN_REMAINING_TURNS:
            break
        help_msg(computernumber=computernumber, guessnumber=guessnumber)
        print(REMAINING_TURNS_MSG.format(turns=turns))
        number_as_command = CMDNumber()
        guessnumber = GuessNumber(number_as_command.get_value)

    result = check_result(turns=turns, level=level)

    # ##########################################
    turn_info = create_turn(
        computer_number=computernumber.value,
        guess_numbers=guessnumber.numbers,
        turns=len(guessnumber.numbers),
        result=result,
    )

    save(turn_info)


if __name__ == "__main__":
    main()
