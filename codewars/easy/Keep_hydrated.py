"""
https://www.codewars.com/kata/582cb0224e56e068d800003c/train/python
Instructions:           Nathan loves cycling.
Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.
"""


def litres(time):
    litres_at_hour = time // 2
    if time < 2:
        litres_at_hour = 0
    return litres_at_hour




   