import sys


class ExtendedList(list):
    def __init__(self, arr):
        super(ExtendedList, self).__init__(arr)

    def __getattr__(self, item):
        if item in ['reversed', 'R']:
            return self[::-1]
        elif item in ['first', 'F']:
            return self[0]
        elif item in ['last', 'L']:
            return self[-1]
        elif item in ['size', 'S']:
            return len(self)
        else:
            raise AttributeError('{} not in attribute'.format(item))

    def __setattr__(self, key, value):
        if key in ['first', 'F']:
            self[0] = value
        elif key in ['last', 'L']:
            self[-1] = value
        elif key in ['size', 'S']:
            if value > len(self):
                self.extend([None for i in range(value - len(self))])
            else:
                del self[value:]
        else:
            raise AttributeError('{} not in attribute'.format(key))


exec(sys.stdin.read())

# if __name__ == '__main__':
#     l = ExtendedList([1, 2, 3])
#     print(l.reversed)
#     print(l.first)
#     l.F = 0
#     print(l)
#     l.append(4)
#     print(l.L)
#     l.size = 2
#     print(l)
