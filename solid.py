# TODO: https://medium.com/@derodu/design-patterns-kiss-dry-tda-yagni-soc-828c112b89ee
# SOLID is an acronym (found by Robert C. Martin) that stands for five different conventions of coding.
# 1. Single-Responsibility Principle (SRP). This principle says that one piece of code (class, function) should do
#   one thing well. By separating concerns, changes to one aspect of a system are less likely to have an impact on
#   other parts, improving code maintainability
# e.x. instead of
#     def math_operations(l):
#         # Compute max
#         print(f'max value in the list is: {max(l)}')
#         # Compute min
#         print(f'min value in the list is: {min(l)}')
#     # we should split the functions and have the main one, e.x. :
#     def get_max(l):
#         # Compute max
#         print(max(l))
#     def get_min(l):
#         # Compute max
#         print(min(l))
#     def main(l):
#         # Compute max
#         get_max(l)
#         # Compute min
#         get_min(l)
#
# so it is easier to find errors, each part of the code is reusable, it is easier to create testing for the code (for
# each function). p.s. tests should be written before the actual implementation

# 2. Open-Close Principle (OCP). 'Software entities should be open for extension but closed for modification' -> you
#   should not modify already existing code if you need a new functionality, simply add what you now need.
# here is the example of using this principle (turning functions into classes):
#
    # import numpy as np
    # from abc import ABC, abstractmethod
    #
    # class Operations(ABC):
    #     '''Operations'''
    #     @abstractmethod
    #     def operation():
    #         pass
    #
    # class Mean(Operations):
    #     '''Compute Max'''
    #     def operation(list_):
    #         print(f"The mean is {np.mean(list_)}")
    #
    # class Max(Operations):
    #     '''Compute Max'''
    #     def operation(list_):
    #         print(f"The max is {np.max(list_)}")
    #
    # class Main:
    #     '''Main'''
    #     @abstractmethod
    #     def get_operations(list_):
    #         # __subclasses__ will found all classes inheriting from Operations
    #         for operation in Operations.__subclasses__():
    #             operation.operation(list_)
    #
    #
    # if __name__ == "__main__":
    #     Main.get_operations([1,2,3,4,5])

# TODO: to read more about the definition of that principle
# 3. Liskov substitution principle (LSP). In simple words: if a subclass redefines a function also present in the
#   parent class, a client-user should not be noticing any differences in behaviour; if in a subclass you redefine a
#   function that is present in the base class, the two new functions ought to have the same behaviour (that doesn't
#   mean that they have to be precisely equal but that a user should expect the same type of result given the same input)
#   The most abstruse (хитромудрий, незрозумілий) principle, there is no standard "template-like" solution

# 4. Interface Segregation Principle (ISP). 'Many client-specific interfaces are better than one general-purpose
#   interface'.
#   The principle suggests that clients should not be forced to depend on interfaces they do not use. It tells us that
#   a class should only have the interface needed and avoid methods that won’t work or that have no reason to be part
#   of that class.
#
#   example:
#     import numpy as np
#     from abc import ABC, abstractmethod
#
#     class Mammals(ABC):
#         @abstractmethod
#         def swim() -> bool:
#             print("Can Swim")
#
#         @abstractmethod
#         def walk() -> bool:
#             print("Can Walk")
#
#     class Human(Mammals):
#         def swim():
#             return print("Humans can swim")
#
#         def walk():
#             return print("Humans can walk")
#
#     class Whale(Mammals):
#         def swim():
#             return print("Whales can swim")
#
#     Human.swim()
#     Human.walk()
#
#     Whale.swim()
#     Whale.walk()
#
#     # Humans can swim
#     # Humans can walk
#     # Whales can swim
#     # Can Walk
#
#   so it is suggested to create more client specific interfaces, e.x.:
#     class Walker(ABC):
#       @abstractmethod
#       def walk() -> bool:
#         return print("Can Walk")
#
#     class Swimmer(ABC):
#       @abstractmethod
#       def swim() -> bool:
#         return print("Can Swim")
#
#     class Human(Walker, Swimmer):
#       def walk():
#         return print("Humans can walk")
#       def swim():
#         return print("Humans can swim")
#
#     class Whale(Swimmer):
#       def swim():
#         return print("Whales can swim")
#
#     if __name__ == "__main__":
#       Human.walk()
#       Human.swim()
#
#       Whale.swim()
#       Whale.walk()

# 5. Dependency Inversion Principle (DIP). "Abstractions should not depend on details. Details should depend on
#   abstractions. High-level modules should not depend on low-level modules. Both should depend on abstractions"
#   Its preferred to depend on an abstraction rather than on another implementation.
