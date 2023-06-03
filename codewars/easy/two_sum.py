"""
https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python
функция должна возврщать список, состоящих из двух индексов чисел, фформирующих
в сумме таргетное число.
"""


def two_sum(numbers, t):
    for i, x in enumerate(numbers):
        for j, y in enumerate(numbers):
            if i != j and x + y == t:
                # print([i, j])
                return [i, j]


# two_sum([1, 2, 3], 4)
# two_sum([1234, 5678, 9012], 14690)
# two_sum([2, 2, 3], 4)
