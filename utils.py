"""
created by Nagaj at 25/04/2021
"""
from constants import HIGH, LOW


def help_msg(computernumber, guessnumber) -> None:
    if guessnumber > computernumber:
        print(HIGH)
    else:
        print(LOW)
