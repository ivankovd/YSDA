import string

CHUNK_SIZE = 4 * 1024 * 1024


def file_generator(filename):
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            yield chunk


def strings(filename, min_str_len=4):
    printable_chars = frozenset(string.printable)
    resp_arr = []
    for chunk in file_generator(filename):
        for c in chunk:
            if chr(c) in printable_chars:
                resp_arr.append(chr(c))
            elif len(resp_arr) > min_str_len:
                resp_string = "".join(resp_arr)
                resp_arr = []
                yield resp_string
            else:
                resp_arr = []
        if len(resp_arr) > min_str_len:
            resp_string = "".join(resp_arr)
            resp_arr = []
            yield resp_string
