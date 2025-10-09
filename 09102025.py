import sys

"""
Fibonacci modified, 

didn't learn anything except for set_int_max_str_digits which is required
for hackerrank to convert int to string to check against their test cases
"""


def fibonacciModified(t1, t2, n):
    sys.set_int_max_str_digits(99999999)
    for _ in range(n - 2):
        res = t1 + t2**2
        t1 = t2
        t2 = res

    return res
