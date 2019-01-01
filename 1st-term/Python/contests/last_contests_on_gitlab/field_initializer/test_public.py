import pytest

from field_initializer import FieldInitializer


def test_one_attribute():
    class A(metaclass=FieldInitializer):
        pass

    a = A(foo=42)
    assert a.foo == 42

def test_multiple_attrs():
    class B(metaclass=FieldInitializer):
        def __init__(self, a, b, c, d=1):
            self.a = 1
            self.b = b
            self.d = d + 1

    b = B(1, 2, 3, foo=4, d=5)
    assert b.a == 1
    assert b.b == 2
    assert b.foo == 4
    with pytest.raises(AttributeError):
        _ = b.c

