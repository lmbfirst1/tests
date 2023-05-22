"""
https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/python
необходимо написать функцию, возвращающую True если число 
является нарциссическим
"""


def narcissistic(value):
    str_value = str(value)
    numbers = len(str_value)
    return (value == sum(int(digit) ** numbers for digit in str_value))


value = 407
narc_format = narcissistic(value)
print(narc_format)
