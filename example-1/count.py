from threading import Thread
from time import perf_counter

def calc_time(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        func(*args, **kwargs)
        end = perf_counter()
        print(f"{func.__name__} took {end - start:.3f}s")
    return wrapper


def count_to_million():
    x = 0
    for _ in range(1_000_000):
        x += 1
    return x


@calc_time
def count_x_times_single_thread(func, n):
    for _ in range(n):
        func()
    print(f"Single-threaded")

@calc_time
def count_x_times_multi_thread(func, n):
    threads = [Thread(target=func) for _ in range(n)]
    for th in threads:
        th.start()
    for th in threads:
        th.join()
    print(f"Multi-threaded")

if __name__ == '__main__':
    count_x_times_single_thread(count_to_million,100)
    count_x_times_multi_thread(count_to_million,100)