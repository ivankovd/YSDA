import pytest

from property_maker import PropertyMaker


def test_example(capsys):
    class C(metaclass=PropertyMaker):
        def get_x(self):
            print("get x")
            return self._x

        def set_x(self, value):
            print("set x")
            self._x = value

    c = C()
    c.x = 1
    assert c.x == 1
    stdout, _ = capsys.readouterr()
    assert stdout == "set x\nget x\n"
