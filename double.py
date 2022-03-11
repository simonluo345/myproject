def double(func):
    def wrapper(*args, **kwargs):
        print("A")
        val = func(*args, **kwargs)
        print('B')
        return val
    return wrapper


@double
def f(a, b=9):
    print(a, b)


@double
def add(x, y):
    return x + y

print(add(2,3))

