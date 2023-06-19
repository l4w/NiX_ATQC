# 1
# open(<file>, mode) function that opens (or creates) a file and return it as a file object
# open() modes:
# 1) 'r' read (default option), opens a file for reading, error if the file doesn't exist
# 2) 'a' append, opens a file for appending, creates the file if it does not exist
# 3) 'w' write, opens a file for writing, creates the file if it does not exist
# 4) 'x' create, creates the specified file, returns an error if the file exist
# In addition you can specify if the file should be handled as binary or text mode:
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)
ex1_file = open('test_file.txt', 'w')
ex1_file.write('Bitcoin price is 24988 dollars, Ethereum price is 1641 dollars!\n')
ex1_file.write('I wish I had 1000 Bitcoins and 2000 Ethereum!\n')
ex1_file.close()

ex1_file = open('test_file.txt', 'r')
ex1_file_content = ex1_file.read()
ex1_file_words = ex1_file_content.split()
ex1_file.close()

nums = []
for i in ex1_file_words:
    if i.isdigit():
        nums.append(int(i))
print(sum(nums))
print('\n')

# 2
biggest_word = ''
for i in ex1_file_words:
    if len(i) > len(biggest_word):
        biggest_word = i
print(biggest_word)
# the best solution
print(max(ex1_file_words, key=len))
print('\n')

# 3
with open('test_file.txt', 'a') as ex3_file:
    ex3_file.write('I am using the context manager!\n')
    ex3_file.write('The second try.')
with open('test_file.txt', 'r') as ex3_file:
    print(ex3_file.read())
print('\n')

# 4
with open('test_file.txt', 'r') as ex4_file, open('test_file_modifies.txt', 'w') as ex4_file_b:
    ex4_first_file_lines = ex4_file.readlines()
    ex4_file_b.write(''.join(ex4_first_file_lines[1:-1]))
with open('test_file_modifies.txt', 'r') as ex4_file_b_read:
    print(ex4_file_b_read.read())

# 5
with open('test_file.txt', 'r') as ex5_file, open('test_file_modifies.txt', 'r') as ex5_file_b:
    ex5_first_file = ex5_file.readlines()
    ex5_second_file = ex5_file_b.readlines()
    smaller_lines_count = min(len(ex5_first_file), len(ex5_second_file))
    for i in range(smaller_lines_count):
        print(f'First file line {i+1}: {ex5_first_file[i] + ex5_second_file[i]}')
