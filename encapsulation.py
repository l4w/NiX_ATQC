# 1
class A:
    __PRIVATE = 'Rusni Pizda'
    _PROTECTED = 'dattebayo'

    def __init__(self, name):
        self.__name = name

    def __private_method_check(self):
        return 2 * 2

    def _protected_method_check(self):
        return 3 * 3


# protected attrs/methods will not be accessible
class B(A):
    pass


ex1_object = A('Bob')
ex1_object_second = B('Robert')
print(ex1_object._PROTECTED)
print(ex1_object._protected_method_check())
print('\n')

# 3
# _ClassName__attribute/methods to get access to a private attr
ex2_object = B('Denys')
print(ex2_object._A__PRIVATE)
print(ex2_object._A__private_method_check())
ex2_object._A__PRIVATE = 5
print(ex2_object._A__PRIVATE)
