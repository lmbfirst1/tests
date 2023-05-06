"""
https://www.codewars.com/kata/57eaeb9578748ff92a000009/train/python
"""

def sum_mix(arr):
    sum = 0
    for i in arr:
        sum = int(i) + sum
    return sum 