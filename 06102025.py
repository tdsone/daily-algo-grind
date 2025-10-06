"""
Another XOR bit game:

You are given two positive integers  and  in binary representation. You should find the following sum modulo :

where operation  means exclusive OR operation, operation  means binary shift to the left.

Please note, that we consider ideal model of binary integers. That is there is infinite number of bits in each number, and there are no disappearings (or cyclic shifts) of bits.

Input Format

The first line contains number   in binary representation. The second line contains number   in the same format. All the numbers do not contain leading zeros.

Output Format

Output a single integer  the required sum modulo .

Sample Input

10
1010
Sample Output

489429555


My thinking so far is to compute T_j where |T_j|
is the number of possible shifts of b to make b at
the j-th position equal to 1.

Then we can say that

cnt1_j : number of shifts that make j-th position 1 after XOR

cnt1_j = (1 - a_j)|T_j| + a_j*((L + 1) - |T_j|)

where L is the number of total shifts and a_j the value of a th pos j
"""
