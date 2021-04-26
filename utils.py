"""
created by Nagaj at 25/04/2021
"""
from constants import HIGH, LOW


def help_msg(computernumber, guessnumber) -> None:
    """
    Basic on value used by the user, program helps him/her with msg.
    :param computernumber: number that computer guess
    :param guessnumber: number that user guess
    :return:
    """
    if guessnumber > computernumber:
        print(HIGH)
    else:
        print(LOW)
