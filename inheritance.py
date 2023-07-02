# 1
class Human:
    __INSTANCE_COUNT = 0
    __INSTANCE = None

    # __new__ is executed BEFORE an instance will be created
    def __new__(cls, *args, **kwargs):
        if not cls.__INSTANCE:
            cls.__INSTANCE = super().__new__(cls)
        return cls.__INSTANCE

    # __init__ is called AFTER an instance will be created
    def __init__(self, age):
        self.age = age

    # one underscores - unavailable
    def __random_sum(self):
        print('hello')

    # one underscore before method - protected
    def random_sum_two(self):
        return 2 * 2


class Man(Human):
    def __init__(self, age, sex):
        super().__init__(age)
        self.sex = sex


x = Human(25)
z = Human(30)
y = Human(50)
z.name = 'John'
print(x.age)
print(z.name)
print(y.name)
# print(x.age)
# print(Human.random_sum_two(Human(30)))
# print(x.random_sum_two())
# y = Human(30)
