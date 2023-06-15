"""
https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python
An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.
"""


def is_isogram(string):
    string = string.lower()
    if len(string) < 2:
        return True

    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False
    return True


def main():
    print(is_isogram("Dermatoglyphics"))
    print(is_isogram("moOse"))
    print(is_isogram("isIsogram"))
    print(is_isogram(""))


if __name__ == '__main__':
    main()
