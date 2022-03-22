def doubler(func):
    def wrapper(*args, **kwargs):
        print("A")
        func(*args, **kwargs)
        func(*args, **kwargs)
        print('B')
        
    return wrapper


@doubler
def func1(a):
    print(a)

func1(2)


