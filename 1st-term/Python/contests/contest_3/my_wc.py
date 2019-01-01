from collections import OrderedDict


def parse_keys(str_keys):
    """
    − m, печатает число символов;
    − l, печатает число строк;
    − L, печатает длину самой длинной строки;
    − w, печатает количество слов;
    """

    need_keys = OrderedDict()
    for key in str_keys.replace('-', '').split():
        need_keys[key] = True
    return need_keys


def wc(text, need_keys):
    response = [-1, -1, -1, -1]
    if 'm' in need_keys:
        # symbol_couter = 0
        # for word in text.split('\n'):
        #     symbol_couter += len(word)
        # response[2] = symbol_couter
        response[2] = len(text)

    if 'l' in need_keys:
        response[0] = len(text.split('\n')) - 1

    if 'L' in need_keys:
        response[3] = max(len(x) for x in text.split('\n'))

    if 'w' in need_keys:
        response[1] = len(text.split())

    return response


# test_text = """  there is one
#     more
# example for
#  problem
# """
# test_text = '  there is one\n    more \nexample for \n problem'

# """-m -l -L -w
#   there is one
#     more
# example for
#  problem
#
#
# """


if __name__ == '__main__':
    need_keys = parse_keys(input())
    # print(need_keys)
    text = ''
    while True:
        try:
            text += input()
            text += '\n'
        except EOFError:
            # text += '\n'
            break
    # response = wc(test_text, need_keys)
    # print('TEST')
    # print(len(test_text))
    response = wc(text, need_keys)
    print(' '.join(str(x) for x in filter(lambda x: x >= 0, response)))
