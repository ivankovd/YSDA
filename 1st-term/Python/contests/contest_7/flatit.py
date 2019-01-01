def flatit(iter_object):
    iter_stack = [iter_object]
    while len(iter_stack) != 0:
        obj = iter_stack.pop(0)
        if '__iter__' in dir(obj):
            if len(obj) > 0 and obj[0] != obj:
                for elem in reversed(obj):
                    iter_stack.insert(0, elem)
            elif len(obj) != 0:
                yield obj
        else:
            yield obj

# if __name__ == '__main__':
#     print(list(flatit([[1, [[2, [5, [6, [2, "test"]]]], 3],
# range(-5, -3, 1)]])))
#     print(list(flatit((1, (2, 3), [4, [5, 6, []], 7]))))
