lower_case = [chr(i) for i in range(ord('a'), ord('z') + 1)]
upper_case = [chr(i) for i in range(ord('A'), ord('Z') + 1)]


def decode_ceaser(str_, shift):
    responce = []
    for char in str_:
        if ord('a') <= ord(char) <= ord('z'):
            responce\
                .append(lower_case[(lower_case
                                    .index(char) + shift) % len(lower_case)])

        elif ord('A') <= ord(char) <= ord('Z'):
            responce\
                .append(upper_case[(upper_case
                                    .index(char) + shift) % len(upper_case)])

        else:
            responce.append(char)

    return "".join(responce)


if __name__ == '__main__':
    shift = int(input())
    str_ = input()
    print(decode_ceaser(str_, shift))
