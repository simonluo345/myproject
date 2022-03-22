def doubler(func):
    def wrapper(*args, **kwargs):
        print("A")
        func(*args, **kwargs)
        func(*args, **kwargs)
        print('B')
        
    return wrapper


@doubler
def func1(a, b):
    print(a, b)


@doubler
def func2(x):
    print(x)

func1(2,3)


