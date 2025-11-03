import sys
from concurrent.futures import ThreadPoolExecutor
from threading import Thread

from utils.utils import calc_time
from utils.cpu import count_x

@calc_time
def count_x_single_thread(func, n):
    for _ in range(n):
        func()
    print(f"Single-threaded {n} times", end=': ')

@calc_time
def count_x_multi_thread(func, n):
    threads = [Thread(target=func) for _ in range(n)]
    for th in threads:
        th.start()
    for th in threads:
        th.join()
    print(f"Multi-threaded {n} threads", end=': ')

@calc_time
def count_x_thread_pool(func, n):
    with ThreadPoolExecutor(max_workers=n) as executor:
        futures = [executor.submit(func) for _ in range(n)]
        for future in futures:
            future.result()
    print(f"Thread Pool {n} threads", end=': ')


if __name__ == '__main__':
    print(f"Is GIL enabled? {sys._is_gil_enabled()}")
    match sys.argv[1:]:
        case ["single", n]:
            count_x_single_thread(count_x, int(n))
        case ["mt", n]:
            count_x_multi_thread(count_x, int(n))
        case ["pool", n]:
            count_x_thread_pool(count_x, int(n))
        case _:
            n = 10
            count_x_single_thread(count_x, n)
            count_x_multi_thread(count_x, n)
            count_x_thread_pool(count_x, n)
