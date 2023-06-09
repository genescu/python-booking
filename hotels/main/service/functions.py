import re


def parser(x, t=None):
    if x is None:
        return None
    else:
        if hasattr(x, 'get_text'):
            x = x.get_text()
        if hasattr(x, 'strip'):
            x = x.strip()
        if hasattr(x, 'split'):
            x = ' '.join(x.split())

    # check for type : int, str
    if t == 'str':
        if not isinstance(x, str):
            return None

    if t == 'float':
        if not is_float(x):
            return None

    if t == 'int':
        if not is_float(x):
            return None
    return x


def is_float(value: any):
    try:
        if isinstance(value, str):
            value = float(value)
        elif isinstance(value, list):
            value = [float(v) for v in value]
        else:
            value = float(value)
        return value
    except ValueError:
        return None
