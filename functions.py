# 1
# was done in loops.py on step 5

# 2
def name_func(name, surname):
    print(f'Hello, my name is {name} {surname}.')


name_func('Denys', 'Romashkin')
name_func(surname='Rashford', name='Markus')
print('\n')


# 3
def args_func(*args):
    print(f'The first car model is {args[0]}.')


args_func('Ford')
print('\n')


# 4
def kwargs_func(**kwargs):
    for key, value in kwargs.items():
        if key == 'name':
            name = kwargs[key]
        elif key == 'age':
            age = kwargs[key]
        else:
            return 'No name or age were provided'
    print(f"{name}'s age is {age}.")


kwargs_func(name='Itachi', age='18')
kwargs_func(name='Naruto', age='14')
print('\n')


# 5
# !!! for age i should have been used None as a default value
def print_person_info(name, surname, age='dummy_value', marital_status='unknown'):
    if age == 'dummy_value':
        print(f'This is {name} {surname}, his/her marital status is {marital_status}.')
    else:
        print(f'This is {name} {surname}, he/she is {age}, his/her marital status is {marital_status}.')


print_person_info(name='Johnny', surname='Depp', age='59', marital_status='unmarried')
print_person_info(name='Johnny', surname='Depp')
print('\n')


# 6
# a factorial of a number (n!) is the product of all positive numbers from 1 to 'n'
# e.x. 5! = 5*4*3*2*1 = 120; 0! = 1

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
