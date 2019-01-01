def sum_divs(num):
    s_divs = 0
    for i in range(1, int(num / 2) + 1):
        if num % i == 0:
            s_divs += i

    # print(s_divs)
    return s_divs


if __name__ == '__main__':
    num = int(input())
    if sum_divs(num) == num:
        print('YES')
    else:
        print('NO')
