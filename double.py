def doubler(func):
    def wrapper(*args, **kwargs):
        print("A")
        func(*args, **kwargs)
        print('B')
        

    return wrapper


@doubler
def func1(a, b):
    print(a, b)


@doubler
def func2(x):
    print(x)

func2(2)
func1(3, 5)

