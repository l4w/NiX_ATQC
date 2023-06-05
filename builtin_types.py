from string import Template

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
print('\n')


def test_fund():
    pass


name = 'Denys'
age = 24
mood = 'sad'
# 1 type of formatting. %s is a placeholder for a str, %d is a placeholder for an int
print('Hello, my name is %s! I am %s years old. Now I feel %s.' % (name, age, mood))
print('\n')

# 2 type of formatting
print('Hello, my name is {1}! I am {0} years old.'.format(name, age))
print('Hello, my name is {0}! But you can also call me {1}.'.format(name, name[:3]))
print('Hello, my name is {}! I am {} years old.'.format(name, age))
print('Hello, my name is {name}! I am {age} years old.'.format(name=test_fund, age=age))
# inserted value can be aligned
print('Align the word {:>10} to the right with spaces.'.format('EGG'))
print('Align the word {:<10} to the left with spaces.'.format('CHICKEN'))
print('Align the word {:^10} to the center with spaces.'.format('PIG'))
print('Align the number {:=10} to the center with spaces.'.format(-5.2))  # for numbers only
print('The universe is {:,} years old.'.format(13800000000))  # a thousand coma separator for num (float, int)
print('The universe is {:_} years old.'.format(13800000000))  # a thousand '_' separator for num (float, int)
print('\n')
# more options here https://www.w3schools.com/python/ref_string_format.asp

# 3 type of formatting (the fastest one)
print(f'Hello, my name is {name}! I am {age} years old.')
# prints today's date with the help of datetime lib
import datetime
today = datetime.datetime.today()
print(f'{today:%B, %d, %Y}')
print(f'No backslash can be used in f-str expression.')
# SyntaxError: f-string expression part cannot include a backslash
print('\n')

# 4 type of formatting using 'from string import Template'. 2 methods:
# 1) substitute(mapping, **kwds)
# 2) safe_substitute(mapping, **kwds) - similar to the first one but doesn't throw KeyError is a key is missing
# 'template' can be used to retrieve Template, e.x. print(template_2.template)
# '$$' to use the dollar symbol in your template
template_var = 'Greenford'
template = Template('I am sitting in $cafe and learning $programming_language.')
print(template.substitute({'cafe': template_var, 'programming_language': 'Python'}))
template_var_2 = 'white noise'
template_2 = Template('I am listening to $music while $action.')
print(template_2.substitute(music=template_var_2, action='studying'))
print(template_2.template + '\n')
