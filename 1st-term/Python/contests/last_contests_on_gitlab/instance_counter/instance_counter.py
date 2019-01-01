class InstanceSemaphore(type):
    def __new__(cls, name, base, attrs):
        return super().__new__(cls, name, base, attrs)

    def __init__(cls, name, base, attrs):
        cls.__max_instance_count__ = 0 if '__max_instance_count__' \
                                          not in attrs else attrs[
            '__max_instance_count__']
        return super().__init__(name, base, attrs)

    def __call__(cls, *args, **kwargs):
        cls.__max_instance_count__ -= 1
        if cls.__max_instance_count__ < 0:
            raise TypeError
        else:
            return super().__call__(*args, **kwargs)
