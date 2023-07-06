# 1
list_with_data = [1, '2', 3.5, True, 4]
print(list_with_data)
print(list_with_data[1:-1])  # Print items from second to penultimate.
print(len(list_with_data))  # Print number of items in list.
list_with_data.append([999])  # Add new item to list and print.
print(list_with_data)
list_with_data.insert(1, 1.5)  # l.insert(index, item)
print(list_with_data)
list_with_data[0] = 1.0  # Change value of item in list and print.
print(list_with_data)
list_with_data[:2] = [1]  # !!! Replace two items of list with one new item.
print(list_with_data)
list_with_data.remove(4)  # Remove item by value and print new list.
print(list_with_data)
list_with_data.pop(2)  # l.pop(index), Remove item by position and print.
print(list_with_data)
print('\n')

# 2
list_one = [1, 2, 3]
list_two = ['japan', 'ukraine']
list_one.append(list_two)  # l.append() inserts a single element into a list, the len of the list is increased by 1
print(list_one)
list_one.extend(list_two)  # l.extend() iterates over its elements and adding each el. to the list, extending it
print(list_one)
print('\n')

# 3
dict_one = {'name': 'Eliezer', 'surname': 'Yudkowsky', 'age': 43}
print(dict_one['name'] + ',', dict_one['age'])  # Print name and age.
print(dict_one.keys())  # Print all keys of dictionary.
print(dict_one.values())  # Print all values of dictionary.
dict_one['age'] = 55
print(dict_one['name'], dict_one['surname'], dict_one['age'])
dict_one['martialStatus'] = 'married'
print(dict_one['name'], dict_one['martialStatus'])
dict_one['children'] = ['David', 'Alice', 'Ashley']
# what was the exact task? how I should have printed them?
print(dict_one['name'], ', '.join(i for i in dict_one['children']))  # 'separator'.join(<one iterable,only str>)
dict_one.pop('age')
print(dict_one.items())  # Print all items of dictionary.
print('\n')

# 4
# tuple with one element is not a tuple, its type will be equal to the type of that one element
my_tuple = ('apple', 42, 3.14, True, [1, 2, 3], '', None, ('a', 'b'), 'android', -10)
print(my_tuple)
print(my_tuple[-4:])  # Print last 4 items.
print(my_tuple.index('android'))  # tuple.index(<value>, start, stop)
my_second_tuple = ('Smaller', 'tuple')
joined_tuple = my_tuple + my_second_tuple
print(joined_tuple)  # Create another tuple, join both tuples and print result.
# Unpack tuple so the first 3 elements unpacked to separate variables
# and rest of elements unpacked to one list element.
x, y, z, *other = joined_tuple
print(x, y, z, other)
print(joined_tuple)
print('\n')
