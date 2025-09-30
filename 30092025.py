#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def isValid(s):
    """
    Valid strings:
    1. All chars appear equally often
    2. Remove just one character at 1 index in the string for s to be case of 1.

    Constraints:
    1. no empty strings
    2. all chars ascii

    Approaches:
    - build mapping from char -> count

    At the end, if all but one count are equal and this count is
    just larger by 1 then return true
    """

    char2count = {}
    for c in s:
        if c in char2count:
            char2count[c] += 1
        else:
            char2count[c] = 1

    print(char2count)

    counts = {}

    for k, v in char2count.items():
        if v in counts:
            counts[v] += 1
        else:
            counts[v] = 1

    print(counts)

    if len(counts.keys()) > 2:
        return "NO"

    if len(counts.keys()) == 1:
        return "YES"

    if len(counts.keys()) == 2:
        """
        There is a case where we have
        counts = {2: 2, 4: 1}
        which means we have two chars with frequency 2 and one char with frequency 4
        for this to work we have to make sure two things: 
            1. abs(key1 - key2) = 1
            2. one of both keys appears once
        """
        items = list(counts.items())
        key0, val0 = items[0]
        key1, val1 = items[1]

        print("items", items)

        if abs(key0 - key1) == 1 and (val0 == 1 or val1 == 1):
            return "YES"
        else:
            return "NO"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = isValid(s)

    fptr.write(result + "\n")

    fptr.close()
