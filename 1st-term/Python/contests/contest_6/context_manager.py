import sys
import traceback
from contextlib import contextmanager


@contextmanager
def supresser(*args, **kwargs):
    try:
        yield
    except args:
        pass


@contextmanager
def retyper(type_from, type_to):
    try:
        yield
    except type_from as e:
        exc_type, exc_repr, exc_tb = sys.exc_info()

        raise type_to(*e.args).with_traceback(exc_tb)


@contextmanager
def dumper(stream):
    try:
        yield
    except Exception as e:
        exc_type, exc_repr, exc_tb = sys.exc_info()
        err_msg = traceback.format_exception_only(exc_type, exc_repr)
        err_pretty_msg = "".join(err_msg)
        stream.write(err_pretty_msg)
        raise
