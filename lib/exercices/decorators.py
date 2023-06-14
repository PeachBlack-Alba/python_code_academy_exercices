
#

def decorator(func):
    def wrapper():
        print('my name is', end=' ')

        return func()
    return wrapper

@decorator
def print_my_name():
    print('Alba')

print_my_name()
