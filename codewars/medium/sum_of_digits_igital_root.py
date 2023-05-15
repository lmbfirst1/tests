"""
https://www.codewars.com/kata/541c8630095125aba6000c00/train/python
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit,
continue reducing in this way until a single-digit number is produced.
The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

"""


def digital_root(n):
    array_of_digit = [int(a) for a in str(n)]
    sum_of_digit = sum(array_of_digit)
    while sum_of_digit > 9:
        second_array = [int(a) for a in str(sum_of_digit)]
        sum_of_digit = sum(second_array)
        if sum_of_digit < 9:
            return sum_of_digit
    else:
        print(sum_of_digit)
        return sum_of_digit



if __name__ ==  '__main__':
    digital_root(1539)
    digital_root(17)
