"""
created by Nagaj at 25/04/2021
"""
from cmd import CMD
from numbers import ComputerNumber, GuessNumber
from validations import LevelValidation

numberObj = CMD()
guessnumber = GuessNumber(numberObj.number_value)
computernumber = ComputerNumber()

print(LevelValidation("tesT").validate_value)