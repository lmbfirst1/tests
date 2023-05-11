"""
https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/train/python
Complete the solution so that it returns true if the first argument(string) 
passed in ends with the 2nd argument (also a string).
Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
"""


def solution(text, ending):
    return True if text[-len(ending):] == ending else False


if __name__ == '__main__':
    solution('samurai', 'ai')
    solution("ninja",   "ja")
    solution("abc",     "abc")
    solution("fails",   "ails")
