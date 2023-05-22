"""
https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python
функция должна возврщать список, состоящих из двух индексов чисел, фформирующих
в сумме таргетное число.
"""

def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]




# test.assert_equals(sorted(two_sum([1,2,3], 4)), [0,2])
# test.assert_equals(sorted(two_sum([1234,5678,9012], 14690)), [1,2])
# test.assert_equals(sorted(two_sum([2,2,3], 4)), [0,1])