"""
created by Nagaj at 26/04/2021
"""
from constants import FAILED, SUCCESS


class Result:
    """
    implement result info
    """

    TEXT = ""


class FailedResult(Result):
    """
       implement failed result info
    """

    TEXT = FAILED


class SuccessResult(Result):
    """
       implement success result info
    """

    TEXT = SUCCESS
