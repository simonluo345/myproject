def doubler(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        
    return wrapper

@doubler #the same as func1 = doubler(func1)
def func1(a):
    print(a)

func1(2)


