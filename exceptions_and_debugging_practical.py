# TASK 1:
def favorite_ice_cream():
    ice_creams = [
        'chocolate',
        'vanilla',
        'strawberry'
    ]
    print(ice_creams[3])

favorite_ice_cream()

# TASK 2:
def some_function():
    msg = 'hello, world!'
    print(msg)
    return msg

# TASK 3:
file_handle = open('myfile.txt', 'w')
file_handle.read()

# TASK 4
def print_message(day):
    messages = {
        'monday': 'Hello, world!',
        'tuesday': 'Today is Tuesday!',
        'wednesday': 'It is the middle of the week.',
        'thursday': 'Today is Donnerstag in German!',
        'friday': 'Last day of the week!',
        'saturday': 'Hooray for the weekend!',
        'sunday': 'Aw, the weekend is almost over.'
    }
    print(messages[day])

def print_friday_message():
    print_message('Friday')

print_friday_message()

# TASK 5
file_handle = open('myfile.txt', 'r')
