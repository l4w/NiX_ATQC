# Abstraction is defined as a process of handling complexity by hiding all unnecessary information from the user.
# e.x. we know the car's color and speed but we don't know to that speed is being reached
# e.x. we are using telegram sending messages and putting reactions to posts but w/o understanding of how its done
# under the hood
# differences with encapsulation:
# - abstraction is a design level process that prevents some parts of the system from being viewed from the very begin.
# - encapsulation is an implementation level process, a 'protecting shield' that prevents data from being accessed
#   by the code outside this shield (e.x. wrapping up of data under a single unit for example with the help of
#   private/protected attr or methods

# empty methods (pass) can be called abstract and classes that have abstract methods can be called abstract
# but Python doesn't support abstract classes by default and that why 'abc' python method comes in handy
# e.x. from abc import ABC, abstractmethod

import random
from abc import ABC, abstractmethod


class Smartphone(ABC):
    @abstractmethod
    def device_starting(self):
        pass


class Android(Smartphone):
    __RANDOM_VAR = 100

    @property
    def RANDOM_VAR(self):
        return self.__RANDOM_VAR

    @RANDOM_VAR.setter
    def RANDOM_VAR(self, value):
        self.__RANDOM_VAR = value

    def device_starting(self):
        return 'This is Android device.'

    # TODO: getter and setter + properties investigation
    @property
    def random_number(self):
        return random.randint(0, 9999)


a = Android()
print(a.random_number)
print(a.RANDOM_VAR)
a.RANDOM_VAR = 1
print(a.RANDOM_VAR)
