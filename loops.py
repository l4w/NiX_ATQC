# 1
list_fruits = ['orange', 'apple', 'banana', 'cherry']
for i in list_fruits:
    print(i, end=' ')
print('\n')

fruit_to_print = 'apple'
for i in list_fruits:
    if i == fruit_to_print:
        print(i, end=' ')
print('\n')

for i in list_fruits:
    print(i, len(i))
print('\n')

# 2
for i in range(2, 100):
    print(i, end=' ')  # end='' a separator for print
print('\n')

# 3
num = 0
while num < 16:
    print(num, end=' ')
    num += 1
print('\n')

# 4
num_two = 3
while num_two <= 33:
    print(num_two, end=' ')
    num_two += 1
print('\n')


# 5
def fruit_iteration():
    for i in list_fruits:
        if i == fruit_to_print:
            break
        else:
            print(i, end=' ')


def fruit_iteration_two():
    for i in list_fruits:
        if i == fruit_to_print:
            continue
        else:
            print(i, end=' ')


fruit_iteration()
print('\n')
fruit_iteration_two()
