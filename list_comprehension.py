# 1
task_1_l1 = [1, 2, 3, 4, 5, -6, -7.2, 8, '-9']
task_1_l2 = [int(i) for i in task_1_l1 if int(i) < 0]
print(task_1_l2)
print('\n')

# 2
task_2_l1 = ['hello', 'apple', 'Japan', 'lol', 'rationality']
task_2_l2 = [i for i in task_2_l1 if len(i) == 11]
print(task_2_l2)
print('\n')

# 3
task_3_l1 = [5, 10, 13, 22, 26, 100, 130]
task_3_l2 = [i for i in task_3_l1 if i % 13 == 0]
print(task_3_l2)
print('\n')

# 4
task_4_l1 = ['Denys', 'vladimir', 'Volodymyr']
task_4_l2 = [i for i in task_4_l1 if i[0] == i[0].upper()]  # here is .isupper() method can be used e.x. i[0].isupper()
print(task_4_l2)
print('\n')

# 5
# TODO: discuss the task with the mentor
# all() func that checks that every element inside is True
task_5_l2 = [i for i in range(120) if all(i % int(digit) == 0 for digit in str(i) if digit != '0')]
print(task_5_l2)
