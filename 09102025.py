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


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

"""
https://www.hackerrank.com/challenges/maxsubarray/problem?isFullScreen=true
"""


def maxSubarray(arr):
    """
    Given an array, find the maximum possible sum among:

    - all nonempty subarrays.
    - all nonempty subsequences.

    Subarray algo is just dp pretending that dp[i] stores the best possible sum that ends with arr[i]

    subsequences.... hm
    - this is just all positive numbers...

    Solution: we can do it in one for loop i think
    """

    N = len(arr)
    dp = [None] * N

    dp[0] = arr[0]
    max_subseq = arr[0]

    for i in range(1, N):
        dp[i] = arr[i] if arr[i] > dp[i - 1] + arr[i] else arr[i] + dp[i - 1]
        if max_subseq < 0 and arr[i] > max_subseq:
            max_subseq = arr[i]
        elif max_subseq >= 0 and arr[i] > 0:
            max_subseq += arr[i]

    max_subarray = max(dp)

    return max_subseq, max_subarray
