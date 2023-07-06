# Polymorphism is about using a single type entity (method, operator, object) to represent different types in
# different scenarios
# e.x. 1 + 1 and 'a' + 'b' - the most common example of polymorphism in python

# 1
class A:
    def multiplying(self):
        print(2 * 2)


class B:
    def multiplying(self):
        print(3 * 3)


class C:
    def multiplying(self):
        print(4 * 4)


def polymorphism_interface(instance):
    instance.multiplying()


a = A()
b = B()
c = C()

print(polymorphism_interface(c))
