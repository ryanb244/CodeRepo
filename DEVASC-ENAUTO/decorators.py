

"""def cool():
    def super_cool():
        return 'I am very cool'

    return super_cool

some_func = cool()

print(some_func())
"""

#passing in a function as an argument to another function

"""def hello():
    return 'Hi Jose!'

def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func())

other(hello)
"""


def new_decorator(original_func):

    def wrap_func():

        print('Some extra code, before the original function')

        original_func()

        print('Some extra code, after the original function!')

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("I want to be decorated!")

func_needs_decorator()




