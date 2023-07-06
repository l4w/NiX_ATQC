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
print('\n')


# 1, 2
class Title:
    EPISODE_DURATION = 25
    EPISODES_NUMBER = 12

    def __init__(self, name, genre, rate):
        self.name = name
        self.genre = genre
        self.rate = rate

    def rate_message(self):
        return f'Anime {self.name} has rating is {self.rate} our of 10.'

    def anime_title_duration(self):
        return self.EPISODE_DURATION * self.EPISODES_NUMBER


class Ova(Title):
    def __init__(self, name, genre, rate, duration):
        super().__init__(name, genre, rate)
        self.duration = duration

    def rate_message(self):
        return f'OVA is better than anime!'


# class Amv(Title, Ova):  - can't inherit from a couple of classes when one is already inherits the first one
#     pass


first_ova = Ova('A Silent Voice', 'Drama/Romance', 8, 130)
first_title = Title('Chainsaw Man', 'Action/Dark Fantasy', 9)
print(first_title.rate_message())
print(first_ova.rate_message())
print(first_ova.anime_title_duration())
print('\n')


# 3
class A:
    EX3_CONST = 1
    EX3_STR_A = 'exercise 3 string'

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def square(self, number):
        return number ** 2


class B:
    EX3_CONST = 2
    EX3_STR_B = 'exercise 3 string, second'

    def __init__(self, third, fourth):
        self.third = third
        self.fourth = fourth

    def square(self, number):
        return number ** 3


class C(B, A):
    pass


ex3_class_c = C(1, 2)
print(ex3_class_c.square(3))
print(ex3_class_c.EX3_CONST)
print(ex3_class_c.EX3_STR_B)
print(ex3_class_c.EX3_STR_A)

# If several classes were inherited from and there are methods, attributes with the same name - will be taken
# elements from the first class specified e.x. A(B, C) B in this case
