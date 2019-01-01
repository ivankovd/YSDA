import functools
import time


def profiler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        this_call_is_main_call = wrapper.is_main_call
        if wrapper.is_main_call:
            wrapper.calls = 0

        wrapper.is_main_call = False

        wrapper.calls += 1

        start = time.time()
        response = func(*args, **kwargs)
        wrapper.last_time_taken = time.time() - start
        if this_call_is_main_call:
            wrapper.is_main_call = True
        return response

    wrapper.is_main_call = True
    return wrapper


@profiler
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


@profiler
def kley(*pararms):
    pararms = list(pararms)
    if len(pararms) == 0:
        return []
    else:
        return pararms[0] + kley(*pararms[1:])

# print(ackermann(3, 2), ackermann.calls, ackermann.calls)
# print(ackermann.calls)
# print(ackermann(3, 2), ackermann.calls)
