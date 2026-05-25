


# just a simple example of decorator
def teacher(func):
    def wrapper():
        print("I am teacher")
        func()
        print("I will teach you somthing")
    return wrapper


@teacher
def student():
    print("you are a student")

student()
# now a logical example means we will divide two num and always bigger no rom smaller num

def log(func):
    def wrapper(*args, **kwargs):
        print("values ", args, kwargs)
        result = func(*args, **kwargs)
        print("result", result)

    return wrapper


def check(func):
    def wrap(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return wrap


@log
@check
def divide(a, b):
    return a / b


@log
@check
def subtract(a, b):
    return a - b


@log
def sum(a, b, c):
    return a + b + c


divide(4, 2)
sum(3, 5, 2)
subtract(78, 5)
