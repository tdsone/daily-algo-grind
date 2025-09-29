"""
https://www.hackerrank.com/challenges/kingdom-division/problem?isFullScreen=true
"""


def kingdomDivision(n, roads):
    import sys

    sys.setrecursionlimit(1_000_000)

    MOD = 10**9 + 7

    if n == 1:
        return 0  # single node can't satisfy "has a same-colored neighbor"

    g = [[] for _ in range(n + 1)]
    for a, b in roads:
        g[a].append(b)
        g[b].append(a)

    def dfs(u, p):
        total = 1
        all_diff = 1
        for v in g[u]:
            if v == p:
                continue
            Sv, Dv = dfs(v, u)
            total = (total * (Sv + Dv)) % MOD
            all_diff = (all_diff * Dv) % MOD
        S_u = total
        D_u = (total - all_diff) % MOD  # ensure 0 under modulo
        return S_u, D_u

    # Root anywhere, say 1
    S_root, D_root = dfs(1, 0)
    return (2 * D_root) % MOD


if __name__ == "__main__":
    pass
