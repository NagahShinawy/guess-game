"""
created by Nagaj at 26/04/2021
"""
from constants import FAILED, SUCCESS


class Result:
    TEXT = ""


class FailedResult(Result):
    TEXT = FAILED


class SuccessResult(Result):
    TEXT = SUCCESS
