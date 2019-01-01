import operator


class RangeIter(object):
    def __init__(self, frm, to, step):
        self.to = to
        self.idx = frm
        self.step = step
        self.operator = operator.ge if step > 0 else operator.le

    def __next__(self):
        if self.operator(self.idx, self.to):
            raise StopIteration
        self.idx += self.step
        return self.idx - self.step


class Range:
    def __init__(self, *args, **kwargs):
        self.start, self.stop, self.step = None, None, None
        for key, value in kwargs:
            setattr(self, key, value)

        if len(kwargs) == 0 and len(args) == 1:
            self.start = 0
            self.stop = args[0]
            self.step = 1
        elif len(kwargs) == 0 and len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1
        else:
            iter_args = iter(args)
            for key in ['start', 'stop', 'step']:
                if getattr(self, key) is None:
                    setattr(self, key, next(iter_args))

    def __len__(self):
        raw_len = int((self.stop - self.start) / self.step)
        return raw_len if raw_len > 0 else 0

    def __contains__(self, item):
        return (item - self.start) % self.step == 0 and \
               self.start <= item < self.stop

    def __iter__(self):
        return RangeIter(self.start, self.stop, self.step)

    def __repr__(self):
        return "Range({}, {}, {})".format(self.start, self.stop, self.step)

    def __getitem__(self, key):
        key = key if key >= 0 else len(self) + key
        return self.start + key * self.step

# if __name__ == '__main__':
#     print(Range(5)[2], Range(5)[-1])
#     print(repr(Range(3)))
#     print(repr(range(3)))
#     for i in Range(3):
#         print(i)
#     print(repr(Range(1, 3)))
#
#     print(repr(Range(1, 3, 4)))
#     for i in Range(1, 10):
#         print(i)
