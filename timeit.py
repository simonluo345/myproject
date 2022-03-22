import time


def calculate_time(func):

    def wrap_func(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("Total time:", t2 - t1)
        return result

    return wrap_func


@calculate_time
def long_time(n):
    for i in range(n):
        for j in range(100000):
            i * j
    time.sleep(2)

long_time(5)
