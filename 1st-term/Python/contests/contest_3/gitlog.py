def formatted_log(len_formatted_log=80):
    log = input()
    ssh = log[:7]
    message = log.split('\t')[-1]
    # print(message)
    points_len = len_formatted_log - len(ssh) - len(message)
    formatted_log = '{}{}{}'.format(ssh,
                                    ''.join(['.' for i in range(points_len)]),
                                    message)
    print(formatted_log)
    # print(len(formatted_log))


if __name__ == '__main__':
    while True:
        try:
            formatted_log()
        except EOFError:
            break
