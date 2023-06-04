var1 = 5
var2 = 8.0

list1 = [1]
list2 = [1]

string1 = '0123.123000000001'
string2 = 'abc'

number = 5
string3 = 'Hello World'

# str.replace('substring', <new str>)
string3 = string3.replace(string3[-number:], '!' * number)
# We took the str w/o last 5 numbers and replaced them with a new symbol * 5
string3 = string3[:-number] + '!' * number
print(string3)

# count(sub, start=None, end=None) can take slices
print(string3.count('o', 1, 9))

# split(<symbol to split>) splits the str, default is space BUT defined symbol is thrown out of the str
str_split = string3.split()
for i in str_split:
    print(i)


def test_fund():
    pass


# TODO IF INTERESTED INVESTIGATE DIFFERENT USAGE OPTIONS OF .format() AND f''
name = 'Denys'
age = 24
mood = 'sad'
# 1 type of formatting. %s is a placeholder for a str, %d is a placeholder for an int
print('Hello, my name is %s! I am %s years old. Now I feel %s.' % (name, age, mood))
# 2 type of formatting
print('Hello, my name is {1}! I am {0} years old.'.format(name, age))
print('Hello, my name is {}! I am {} years old.'.format(name, age))
print('Hello, my name is {name}! I am {age} years old.'.format(name=test_fund, age=age))
# 3 type of formatting
print(f'Hello, my name is {name}! I am {age} years old.')
