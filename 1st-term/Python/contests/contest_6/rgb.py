import re

simple_re = re.compile(r'(\s*\d+,?\s*){3}')
hex_re = re.compile(r'#[A-Fa-f0-9]{6}')
permutation_re = re.compile(r'[r|g|b]{3}\((\s*\d+,?\s*){3}\)')
percent_re = re.compile(r'[0-9]+%')


def percent2value(persent_string):
    return str(int(int(persent_string[:-1]) / 100 * 255))


def hex2rgb(hex_color):
    hex_color = hex_color.strip('#')
    rgb_color = '{} {} {}'.format(
        *[int(hex_color[i:i + 2], 16) for i in (0, 2, 4)]
    )
    return rgb_color


def permutation2rgb(perm_color):
    permutation = {}
    for i, col in enumerate(re.search('[r|g|b]{3}', perm_color).group()):
        permutation[col] = i

    colors = re.search(simple_re, perm_color).group().split(', ')
    for col in colors:
        if int(col) > 255:
            return 'ERROR'
    return ' '.join([colors[permutation[col]].strip() for col in 'rgb'])


def converter(color):
    if re.match(simple_re, color):
        return color
    if re.match(hex_re, color):
        return hex2rgb(color)

    if len(re.findall(percent_re, color)) not in [0, 3]:
        return 'ERROR'
    color = re.sub(percent_re, lambda x: percent2value(x.group()), color)
    if re.match(permutation_re, color):
        return permutation2rgb(color)

    return 'ERROR'


if __name__ == '__main__':
    color = input()
    response_color = converter(color)
    print(response_color)
