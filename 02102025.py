# Full variant that also returns the DP matrix for display purposes
def nw_align_full(a: str, b: str):
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    prev = [[-1] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = i
        prev[i][0] = 1
    for j in range(1, m + 1):
        dp[0][j] = j
        prev[0][j] = 2

    for i in range(1, n + 1):
        ai = a[i - 1]
        for j in range(1, m + 1):
            bj = b[j - 1]
            cost_sub = 0 if ai == bj else 1
            candidates = [
                (dp[i - 1][j - 1] + cost_sub, 0),
                (dp[i - 1][j] + 1, 1),
                (dp[i][j - 1] + 1, 2),
            ]
            dp[i][j], prev[i][j] = min(candidates)

    i, j = n, m
    A, B = [], []
    while i > 0 or j > 0:
        p = prev[i][j]
        if p == 0:
            A.append(a[i - 1])
            B.append(b[j - 1])
            i -= 1
            j -= 1
        elif p == 1:
            A.append(a[i - 1])
            B.append("-")
            i -= 1
        else:
            A.append("-")
            B.append(b[j - 1])
            j -= 1
    A.reverse()
    B.reverse()
    return dp[n][m], "".join(A), "".join(B), dp


def format_dp_matrix(dp, a: str, b: str) -> str:
    n, m = len(a), len(b)
    col_headers = ["-"] + list(b)
    lines = []
    header = "    " + " ".join(f"{ch:>3}" for ch in col_headers)
    lines.append(header)
    for i in range(n + 1):
        row_label = "-" if i == 0 else a[i - 1]
        row_vals = " ".join(f"{dp[i][j]:>3}" for j in range(m + 1))
        lines.append(f"{row_label:>3} {row_vals}")
    return "\n".join(lines)


def format_alignment_spaced(A: str, B: str) -> str:
    return "\n".join([" ".join(A), " ".join(B)])


# Assume nw_align(a, b) -> (dist, A, B) is already defined.

TESTS = [
    # (a, b, expected_distance, expected_A, expected_B)
    # Empty / trivial
    ("", "", 0, "", ""),
    ("", "ABC", 3, "---", "ABC"),
    ("ABC", "", 3, "ABC", "---"),
    # Exact match / simple substitution
    ("ABC", "ABC", 0, "ABC", "ABC"),
    ("ABC", "ABD", 1, "ABC", "ABD"),
    # Classic textbook examples
    ("GATTACA", "GCATGCU", 4, "GATTACA", "GCATGCU"),
    ("kitten", "sitting", 3, "kitten-", "sitting"),
    # Your example
    ("FLIEGE", "LIEBEN", 3, "FLIEGE-", "-LIEBEN"),
    # Gap-only skew
    ("AAAA", "AA", 2, "AAAA", "--AA"),
    ("ACGT", "ACG", 1, "ACGT", "ACG-"),
    ("ACG", "ACGT", 1, "ACG-", "ACGT"),
    # Completely different strings
    ("ABCD", "WXYZ", 4, "ABCD", "WXYZ"),
    # Tie-heavy case to exercise deterministic arrows
    ("ABAB", "BABA", 2, "-ABAB", "BABA-"),
]

# Quick ad-hoc run without pytest:
if __name__ == "__main__":
    for a, b, exp_d, exp_A, exp_B in TESTS:
        d, A, B, dp = nw_align_full(a, b)
        ok = (d == exp_d) and (A == exp_A) and (B == exp_B)
        print(f"{a!r} vs {b!r}: dist={d} {'OK' if ok else 'FAIL'}")
        if not ok:
            print(" expected:", exp_d, exp_A, exp_B)
            print(" got     :", d, A, B)
        print("DP matrix:")
        print(format_dp_matrix(dp, a, b))
        print("Alignment:")
        print(format_alignment_spaced(A, B))
        print()


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def _is_valid_block(s) -> bool:
            return

        def _get_valid_IPs(start: str, end: str):
            print("start", start, "end", end)
            # base cases
            if start == "":
                return [end]

            # recursion
            valid_ips = []

            # case 1: insert .
            if end.find(".") > -1:
                prev_block = end[0 : end.find(".")]
            else:
                prev_block = end

            print("prev_block", prev_block)

            conditions = [
                len(start) >= 1,  # valid IP cannot end with .
                not (len(start) > (4 - end.count(".") - 1) * 3),
                not (prev_block.startswith("0") if len(prev_block) > 1 else False),
                not (prev_block == ""),  # no repeat .
            ]

            if not (prev_block == ""):
                conditions.append(
                    int(prev_block) <= 255  # no blocks larger 255
                )

            print("conditions\n", conditions)

            if all(conditions):
                valid_ips.extend(_get_valid_IPs(start, "." + end))

            if _is_valid_block(start[-1] + end):
                valid_ips.extend(_get_valid_IPs(start[0:-1], start[-1] + end))

            return valid_ips

        if len(s) > 12:
            return []

        valid_IPs = _get_valid_IPs(s[0:-1], s[-1])  # 2552551113, 5
        print(valid_IPs)
        return valid_IPs
