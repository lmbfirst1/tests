"""
https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.

"""

def make_readable(seconds):
    if seconds < 0 or seconds > 359999:
        raise ValueError("Некорректное значение секунд.")
    
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 60)
    
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"