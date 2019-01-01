import pytest

from instance_counter import InstanceSemaphore

def test_simple():
    class A(metaclass=InstanceSemaphore):
        __max_instance_count__ = 2

    a_first = A()
    a_second = A()

def test_extra_instannces():
    class B(metaclass=InstanceSemaphore):
        __max_instance_count__ = 1

    b_first = B()
    with pytest.raises(TypeError):
        b_second = B()

