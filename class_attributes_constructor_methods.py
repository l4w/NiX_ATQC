# 1
class FirstClass:
    CLASS_NAME = 'Robert'
    CLASS_AGE = 22

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def instance_attr(self):
        return str(self.name) + ' ' + str(self.age)

    def age_sum(self):
        return sum((self.CLASS_AGE, self.age))


x = FirstClass('Denys', 24)
x.CLASS_AGE = 30
x.test_attr = 'hello'
print(x.test_attr)

print(x.CLASS_AGE)  # new attribute of the instance is created
print(x.__dict__)  # contains all instance attr
print(x.__class__.__name__)  # returns the parent class name
print(__file__)  # returns absolute path to the file
print(FirstClass.__dict__)
print(FirstClass.CLASS_AGE)

print('\n')
print(x.instance_attr())
print(x.age_sum())
