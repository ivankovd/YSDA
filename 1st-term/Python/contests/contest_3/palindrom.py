def is_palindrom(s):
    return s == s[::-1]


def calc_cnt_cymbols(s):
    len_s = len(s)
    for i in range(len_s):
        str_now = s[i:]
        if is_palindrom(str_now):
            return i

    return len_s


if __name__ == '__main__':
    s = input()
    left = calc_cnt_cymbols(s)
    right = calc_cnt_cymbols(s[::-1])
    print(min(left, right))
