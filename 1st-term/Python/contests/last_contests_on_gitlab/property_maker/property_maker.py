class PropertyMaker(type):
    def __new__(cls, name, bases, attrs):
        return super().__new__(cls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        methods = {key: value for key, value in attrs.items()
                   if callable(value)}

        _get_methods = {key[4:]: value for key, value in methods.items()
                         if key.startswith('get_')}

        _set_methods = {key[4:]: value for key, value in methods.items()
                         if key.startswith('set_')}

        _s_get_methods = set(_get_methods)
        _s_set_methods = set(_set_methods)
        _s_g_methods = _s_get_methods.intersection(_s_set_methods)

        for key in _s_get_methods:
            if key not in _s_g_methods:
                setattr(cls, key, property(fget=_get_methods[key]))

        for key in _s_set_methods:
            if key not in _s_g_methods:
                setattr(cls, key, property(fset=_set_methods[key]))

        for key in _s_g_methods:
            setattr(cls, key, property(fget=_get_methods[key],
                                       fset=_set_methods[key]))
        return super().__init__(name, bases, attrs)
