"""
https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python
функция должна возврщать список, состоящих из двух индексов чисел, фформирующих
в сумме таргетное число.
"""

def two_sum(numbers, target):
	true_indexes = []
	extra_element = sum(numbers) - target
	for i in numbers:
		if i != extra_element:
			index = numbers.index(i) 
			true_indexes.append(index)
		
	return true_indexes