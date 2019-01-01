def strong_or_weak(password):
    if len(password) < 8 or len(set(password)) < 4 or\
            'anna' in password.lower():
        return 'weak'

    password_set = set(password)
    lower_upper_number = [False, False, False]
    for element in list(password_set):
        if ord('a') <= ord(element) <= ord('z'):
            lower_upper_number[0] = True
        elif ord('A') <= ord(element) <= ord('Z'):
            lower_upper_number[1] = True
        elif ord('0') <= ord(element) <= ord('9'):
            lower_upper_number[2] = True
    if sum(lower_upper_number) == 3:
        return 'strong'
    else:
        return 'weak'


if __name__ == '__main__':
    password = input()
    print(strong_or_weak(password))
