# 1
x = 5
y = 9.5
x += y  # assign cannot be written inside print() func
print(x)
print('\n')

# 2
int_10 = 10
# ZeroDivisionError: division by zero
# print(int_one / 0)
string_one = '10'
# str can be divided
# print(string_one / 0)

# 3
# casting in Python is done using constructor functions e.x. int(), float(), str()
int_10_second = int(10)
string_japan = str('Japan')
float_5_5 = float(5.5)
print(int_10_second < float_5_5)
print(int_10_second == int_10)
# print(string_two < int_two)  # TypeError: '>' '<' not supported between instances of 'str' and 'int'
print(string_japan != int_10_second)  # '==' '!=' not supported between instances of 'str' and 'int'
print('\n')

# 4
# done in the step (1)

# 5
string_onion = 'Onion'
string_tomato = 'Tomato'
print(string_tomato > string_onion)  # len(string_tomato) is bigger than len(string_onion)
# other operators behaves the same as with nums (==, != operators)
string_vegetable_combination = string_tomato + ' ' + string_onion  # words concatenation
print(string_vegetable_combination)
