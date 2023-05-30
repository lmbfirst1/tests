"""
https://www.codewars.com/kata/515e271a311df0350d00000f/train/python
"""


def square_sum(numbers):
    sum = 0
    for i in numbers:
        squere = i ** 2
        sum += squere
    return sum

numbers = [-1, -2]
sum = square_sum(numbers)
print(sum)




        # test.assert_equals(square_sum([1,2]), 5)
        # test.assert_equals(square_sum([0, 3, 4, 5]), 50)
        # test.assert_equals(square_sum([]), 0)
        # test.assert_equals(square_sum([-1,-2]), 5)
        # test.assert_equals(square_sum([-1,0,1]), 2)
