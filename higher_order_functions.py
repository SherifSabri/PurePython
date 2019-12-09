def py_map(in_list, func):
    for elem in in_list:
        yield func(elem)


def py_filter(in_list, pred):
    for elem in in_list:
        if pred(elem):
            yield elem


def py_take_while(in_list, pred):
    """return all elements in a list until the condition fails"""
    for elem in in_list:
        if not pred(elem):
            break
        else:
            yield elem


def py_foldl(in_list, func, acc):
    if in_list is None or len(in_list) == 0:
        return acc
    return py_foldl(in_list[1:], func, func(acc, in_list[0]))


def py_foldr(in_list, func, acc):
    if in_list is None or len(in_list) == 0:
        return acc
    return func(in_list[0], py_foldr(in_list[1:], func, acc))


def py_curry(*args):
    """function curring, i.e: partial functions"""
    for func in args:
        yield lambda y: func(y)


def py_apply(func_f, func_g):
    """function application, i.e: composition"""
    return lambda x: func_f(func_g(x))
