# There are 2 types of errors: syntax and exceptions (appear during runtime)
# 1
try:
    print(10 * 5)
    print(10 / 0)
    print(10 * 10)
except ZeroDivisionError as e:
    print(f'The following exception occurred: {str(e)}.')
finally:
    print('\n')


# 2
# super() function that is used to give access to the methods of a parent class. it returns a temp object of the
# parent class when used
# custom exceptions are usually used paying attention to its name
class CustomException(Exception):
    def __init__(self, message, condition):
        super().__init__(message)
        self.condition = condition

    def __str__(self):
        return f'{super().__str__()} (Condition: {self.condition})'


def some_func():
    x = 2
    if x == 2:
        raise (CustomException('Incorrect value', 'x == 2'))


some_func()
