import itertools


def transpose(arr):
    return zip(*arr)


def uniq(arr):
    unique = set()
    for elem in itertools.filterfalse(lambda x: x in unique, arr):
        unique.add(elem)

    return list(unique)


def dict_merge(*dicts):
    return dict([
        i for i in itertools.chain.from_iterable(d.items() for d in dicts)
    ])


def product(u, v):
    return sum(map(lambda i: i[0] * i[1], zip(u, v)))

# if __name__ == '__main__':
#     print(list(transpose([(1, 2), (3, 4), (5, 6)])))
#     print(list(uniq([1, 2, 3, 3, 1, 7])))
#     print(dict_merge({1: 2}, {2: 2}, {1: 1}))
#     print(product([1, 2, 3], [4, 5, 6]))
