#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    (a, b) = (0, 0)
    tuple_c = ()
    for idx in range(0, 2):
        if not tuple_a[idx]:
            if not tuple_b[idx]:
                tuple_c = tuple_c + (a + b)
            b = tuple_b[idx]

            tuple_c += a + b
