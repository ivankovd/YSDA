import functools
import sys


def takes(*params):
    def wraps(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for arg_type, arg in zip(params, args):
                if not isinstance(arg, arg_type):
                    raise TypeError
            return func(*args, **kwargs)

        return wrapper

    return wraps


exec(sys.stdin.read())
