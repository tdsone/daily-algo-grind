class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        """
        Approach:
        - DP
        - Start filling from back:
            - dp[i] is the sum from i to end
        """

        N = len(energy)
        dp = [None] * N

        dp[-1] = energy[-1]

        max_sum = dp[-1]

        for i in range(N - 1, -1, -1):
            if i + k < N:
                dp[i] = energy[i] + dp[i + k]
            else:
                dp[i] = energy[i]

            if dp[i] > max_sum:
                max_sum = dp[i]

        return max_sum
