"""
https://www.hackerrank.com/challenges/sherlock-and-cost/problem
"""


def cost(B: list[int]) -> int:
    """
    Insight: for three consecutive numbers a, b, c in A
    you maximize S by pushing b to one endpoint.

    Thus, all values will have picked one of the endpoints

    Something with 2 state DP, where H stores the max until here, when picking A[i] = B[i] and L stores max until now when picking 1.
    """

    N = len(B)

    L = [-1] * N
    H = [-1] * N

    L[0], H[0] = 0, 0

    # Iterate over all elements in B
    for i in range(1, len(B)):
        L[i] = max(
            # picked 1 before, thus picking one
            # here doesn't add to abs diff
            L[i - 1] + abs(1 - 1),
            # picked B[i - 1] before, thus picking one
            # here increases sum
            H[i - 1] + abs(B[i - 1] - 1),
        )
        H[i] = max(L[i - 1] + abs(B[i] - 1), H[i - 1] + abs(B[i - 1] - B[i]))

    return max(H[N - 1], L[N - 1])


if __name__ == "__main__":
    pass
