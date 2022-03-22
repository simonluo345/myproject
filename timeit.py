from time import time


def calculate_time(func):

    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print("Total time:", t2 - t1, "s")
        return result

    return wrap_func


def long_time(n):
    for i in range(n):
        for j in range(100000):
            i * j


long_time(5)
