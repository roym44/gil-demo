import sys
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

from utils import calc_time

def count_x():
    x = 0
    for _ in range(10_000_000):
        x += 1
    return x


@calc_time
def count_x_multi_thread(func, n, t):
    with ThreadPoolExecutor(max_workers=n) as executor:
        futures = [executor.submit(func) for _ in range(t)]
        for future in futures:
            future.result()
    print(f"Thread Pool {n} threads {t} times", end=': ')

@calc_time
def count_x_multi_process(func, n, t):
    with ProcessPoolExecutor(max_workers=n) as executor:
        futures = [executor.submit(func) for _ in range(t)]
        for future in futures:
            future.result()
    print(f"Process Pool {n} processes {t} times", end=': ')


if __name__ == '__main__':
    print(f"Is GIL enabled? {sys._is_gil_enabled()}")
    match sys.argv[1:]:
        case ["mt", t, n]:
            count_x_multi_thread(count_x, int(n), int(t))
        case ["mp", t, n]:
            count_x_multi_process(count_x, int(n), int(t))
        case _:
            t = 10
            n = 20
            count_x_multi_thread(count_x, n, t)
            count_x_multi_process(count_x, n, t)
