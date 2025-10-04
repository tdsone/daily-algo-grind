#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'primeXor' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#


def primeXor(a):
    # Write your code here

    """
    Approach 1:
    - find all the multisets
    - check each for it being prime

    The way to get all multisets is to simply enumerate a bitmask with len(a) bits

    Q: suppose [4, 2, 3, 5]. Does 4 not being prime make any XOR
    with other elements in the set make it not be prime?

    How is primality being influenced by XOR?
    [100, 010, 011, 011]
    Observations:
    - XOR between one prime one not prime can be prime (e.g. 4 XOR 3 = 111 = 7 is prime)
    - XOR between two primes 101 XOR 011 = 110 = 6 can be not prime
    - two not primes 8 XOR 4 = 1000 XOR 0100 = 1100 = 12 is not prime

    Two odd prime numbers -> even number not prime => two primes XORed make a non-prime
    - even and odd

    Also: all a are between 3500 and 4500. There is a fixed number of
    primes between them:

    3511, 3517, 3527, 3529, 3533, 3539, 3541, 3547, 3557, 3559, 3571, 3581, 3583, 3593, 3607, 3613, 3617, 3623, 3631, 3637, 3643, 3659, 3671, 3673, 3677, 3691, 3697, 3701, 3709, 3719, 3727, 3733, 3739, 3761, 3767, 3769, 3779, 3793, 3797, 3803, 3821, 3823, 3833, 3847, 3851, 3853, 3863, 3877, 3881, 3889, 3907, 3911, 3917, 3919, 3923, 3929, 3931, 3943, 3947, 3967, 3989, 4001, 4003, 4007, 4013, 4019, 4021, 4027, 4049, 4051, 4057, 4073, 4079, 4091, 4093, 4099, 4111, 4127, 4129, 4133, 4139, 4153, 4157, 4159, 4177, 4201, 4211, 4217, 4219, 4229, 4231, 4241, 4243, 4253, 4259, 4261, 4271, 4273, 4283, 4289, 4297, 4327, 4337, 4339, 4349, 4357, 4363, 4373, 4391, 4397, 4409, 4421, 4423, 4441, 4447, 4451, 4457, 4463, 4481, 4483, 4493

    Any XOR operation between numbers makes the result at max the 2^bits+1 - 1

    4500 = 0b1,00,01,10,01,01,00 -> 13 bits -> 2^14 - 1 = 16383

    The thing that we would recompute every time would be the XOR computation.
    XOR is associative so we can simply cache the results
    """


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        a = list(map(int, input().rstrip().split()))

        result = primeXor(a)

        fptr.write(str(result) + "\n")

    fptr.close()
