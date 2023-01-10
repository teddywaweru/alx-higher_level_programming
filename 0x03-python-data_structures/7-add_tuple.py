#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    (a, b) = (0, 0)
    list_c = []
    for idx in range(0, 2):
        if not tuple_a[idx]:
            if not tuple_b[idx]:
                list_c.append(0)
            else:
                b = tuple_b[idx]
                list_c.append(0 + b)
        else:
            a = tuple_a[idx]
            if not tuple_b[idx]:
                list_c.append(0 + a)
            else:
                b = tuple_b[idx]
                list_c.append(a + b)

    tuple_c = tuple(list_c)

    return tuple_c
