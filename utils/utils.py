from time import perf_counter

def calc_time(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        func(*args, **kwargs)
        end = perf_counter()
        print(f"{func.__name__} took {end - start:.3f}s")
    return wrapper


def async_calc_time(func):
    async def wrapper(*args, **kwargs):
        start = perf_counter()
        await func(*args, **kwargs)
        end = perf_counter()
        print(f"{func.__name__} took {end - start:.3f}s")
    return wrapper