from itertools import chain, combinations


class FieldInitializer(type):
    def __call__(cls, *args, **kwargs):
        list_keys = list(kwargs.keys())
        key_sets = chain.from_iterable(combinations(list_keys, i)
                                       for i in range(len(list_keys) + 1))

        for key_set in reversed(list(key_sets)):
            set_kwargs = {key: kwargs[key] for key in key_set}
            try:
                instance = super().__call__(*args, **set_kwargs)
            except TypeError:
                pass
            else:
                break

        for key, value in kwargs.items():
            try:
                getattr(instance, key)
            except AttributeError:
                setattr(instance, key, value)
        return instance
