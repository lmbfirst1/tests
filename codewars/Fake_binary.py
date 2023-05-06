"""
https://www.codewars.com/kata/57eae65a4321032ce000002d/train/python
"""
def fake_bin(x):
    result = ""
    for num in x:
        if int(num) < 5:
            result = result + "0"
        else:
            result = result + "1"
    return result


# import string
#                                       красивое решение
# def fake_bin(s):
#     return s.translate(string.maketrans('0123456789', '0000011111'))


x = "45385593107843568"
new_x = fake_bin(x)
print(new_x)

