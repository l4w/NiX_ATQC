# 1
# lambda has to be assigned

# TODO: def myfunc(n):
#   return lambda a : a * n
lambda_function = lambda x, l: [x * i for i in l]
print(lambda_function(5, [6, 7, 8]))
print('\n')

# 2

# TODO: go through #2 again
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
is_odd = lambda x: x % 2 != 0
results = [is_odd(num) for num in numbers]
# zip(<iterable parameters>) creates list
for num, result in zip(numbers, results):
    print(f"Number {num}: {not result}")
print('\n')

# 3

from datetime import datetime

var_one = datetime.now()
lambda_datetime = lambda x: x.strftime('%Y, %m, %d')
print(lambda_datetime(var_one))
print('\n')

# 4
# map(<func/lamb>, <iterable object>)

print(list(map(lambda x: x * 2, numbers)))
print('\n')

# 5
# filter()

updated_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(updated_numbers)
print('\n')

# PRACTICE:
# * lambda:
print('PRACTICE STARTS\n')

print('Exercise 1. Write a lambda function that takes a list of numbers '
      'as input and returns a new list containing only the odd numbers.')
ex_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ex_odd_list = list(filter(lambda x: x % 2 != 0, ex_list))
print(ex_odd_list)
print('\n')

print('Exercise 2. Write a lambda function that takes a list of dictionaries as input '
      'and returns a new list containing the dictionaries sorted by a specific key in ascending order.')
ex_dict_list = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Charlie', 'age': 20},
    {'name': 'Bob', 'age': 30}
]
ex_sorted_dict_list = sorted(ex_dict_list, key=lambda x: x['age'])
print(ex_sorted_dict_list)
print('\n')

print('Exercise 3. Write a lambda function that takes a list of numbers as input'
      ' and returns a new list containing the square of each element.')
ex_squared_list = list(map(lambda x: x ** 2, ex_list))
print(ex_squared_list)
print('\n')

print('Exercise 4. Write a lambda function that takes a list of strings as input '
      'and returns a new list containing only the strings that are palindromes.')
ex_str_list = ['apple', 'banana', 'cherry', 'abba', 'elderberry', 'radar']
ex_palindrome_str_list = list(filter(lambda x: x == x[::-1], ex_str_list))
print(ex_palindrome_str_list)
print('\n')

print('Exercise 5. Write a lambda function that takes two lists of equal length as input '
      'and returns a dictionary where the elements from the first list are used as keys '
      'and the elements from the second list are used as values.')
ex5_same_length_list_one = ['Joseph', 'Steven', 'Daniel']
ex5_same_length_list_two = ['doctor', 'lawyer', 'engineer']
ex5_list_dict = dict(map(lambda l1, l2: (l1, l2), ex5_same_length_list_one, ex5_same_length_list_two))
print(ex5_list_dict)
