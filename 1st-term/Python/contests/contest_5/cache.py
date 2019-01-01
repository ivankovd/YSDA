import functools
from collections import OrderedDict


def cache(n):
    cache_dict = OrderedDict()

    def wraps(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            s_args = [str(i) for i in args]
            s_kwargs = [
                ''.join([str(i[0]), str(i[1])]) for i in list(kwargs.items())
            ]
            params = ''.join(s_args + s_kwargs)
            if params not in cache_dict:
                if len(cache_dict) == n:
                    cache_dict.pop(list(cache_dict.keys())[0])
                cache_dict[params] = func(*args, **kwargs)
            return cache_dict[params]

        return wrapper

    return wraps
