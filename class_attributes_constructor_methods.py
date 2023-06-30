# 1
class FirstClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    class_name = 'Robert'
    class_age = 22

    def instance_attr(self):
        return str(self.name) + ' ' + str(self.age)

    def age_sum(self):
        return sum((self.class_age, self.age))


x = FirstClass('Denys', 24)
print(x.instance_attr())
print(x.age_sum())
