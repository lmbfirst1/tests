"""
https://www.codewars.com/kata/523f5d21c841566fde000009/train/python
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.
If a value is present in b, all of its occurrences must be removed from the other:

"""
def array_diff(a, b):
    common_numbers = set(a) and set(b)
    result = [num for num in a if num not in common_numbers]
    return result 

def main():
    array_diff([1,2,2,2,3],[2])


if __name__ == '__main__':
    main()
