def doubler(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        
    return wrapper


@doubler
def func1(a):
    print(a)

func1(2)


