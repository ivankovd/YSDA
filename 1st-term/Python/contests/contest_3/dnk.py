def create_compl_dnk(dnk):
    replacer = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }
    return ''.join(list(map(lambda x: replacer[x], dnk[::-1])))


if __name__ == '__main__':
    dnk = input()
    print(create_compl_dnk(dnk))
