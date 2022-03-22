def doubler(func):
    def wrapper(*args, **kwargs):
        print("A")
        val = func(*args, **kwargs)
        print('B')
        return val
    return wrapper


@doubler
def f(a, b=9):
    print(a, b)


@doubler
def add(x, y):
    return x + y

print(add(2,3))

