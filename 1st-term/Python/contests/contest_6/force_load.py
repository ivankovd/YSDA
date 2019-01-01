import traceback


def force_load(module_name):
    with open("{}.py".format(module_name)) as f:
        lines = f.readlines()

    while True:
        code = "".join(lines)
        try:
            exec(code)
        except Exception as e:
            frame_summary = traceback.extract_tb(e.__traceback__)[-1][1]
            lineno = getattr(e, 'lineno', frame_summary)
            del lines[lineno - 1]
        else:
            break

    ldict = {}
    exec("".join(lines), globals(), ldict)
    return ldict
