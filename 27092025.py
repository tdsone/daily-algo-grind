"""
https://www.hackerrank.com/challenges/sherlock-and-cost/problem
"""


def countArray(n, k, x):
    """
    Construct array A of length n where:
    - A[0] = 1
    - A[n - 1] = x
    - 1 <= A[i] <= k
    - A[i] != A[i+1]

    Return the count of all possible ways to construct A

    Approach
    dp[i]: number of valid ways to construct array up until here

    at each position there is k - 1 options
    e.g.
    dp[0] = 1
    dp[1] = dp[0] * (k - 1) e.g. 1 * 2
    then again, for each number, there is 2 other valid options
    dp[2] = dp[1] * (k - 1)
    now, we get to the last element which has to be x
    we now have to delete all paths that led to here, which depend on having
    x in position n - 1, since if 1 <= x <= k, then that means we
    have to subtract 1/k paths from dp[i-1] to get the result
    """

    dp = [0] * n

    dp[0] = 1
    init_shares = [0] * k
    init_shares[0] = 1
    shares = [[0] * k] * n  # tracks the share of each number at position i
    shares[0] = init_shares

    for i in range(1, n - 1):
        dp[i] = dp[i - 1] * (k - 1)
        tmp_shares = []

        for s in shares[i - 1]:
            nom = 1 - s
            # every entry in shares[i - 1] will appear k times in shares[i]
            denom = k - 1
            tmp_shares.append(nom / denom)
        shares[i] = tmp_shares

    return int(dp[n - 2] * (1 - shares[n - 2][x - 1]))


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
