def func_counter(func):
    def wrapper(*args):
        wrapper.counter += 1
        func(*args)

    wrapper.counter = 0
    return wrapper


@func_counter
def foo(y):
    return y + 2 ** 3 - 34


foo(2)
foo(3)
foo(5)
foo(4)
print(foo.counter)  # expect 4 to be printed
