def get_pingvins(n):
    pingvinogenerator = [
        '   _~_    ',
        '  (o o)   ',
        ' /  V  \  ',
        '/(  _  )\ ',
        '  ^^ ^^   '
    ]

    answer = []
    for i in range(5):
        answer.append(pingvinogenerator[i] * n)

    print('\n'.join(answer))


if __name__ == '__main__':
    n = int(input())
    get_pingvins(n)
