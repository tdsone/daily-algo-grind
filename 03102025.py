from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Assumption:
        - max_sum will end on some index j
        - max_sum_j is the max_sum when the sum ends on index j (inclusive)
        - if nums[j] + max_sum_j-1 > nums[j] then max_sum_j = nums[j] + max_sum_j-1
        - else it's just nums[j]

        But what if we have something like:
        - dp = [2, -1, ?]
        - nums = [2, -3, 3]
        -> wouldn't I have to go back two sections because 2 - 1 > 0
        -> not in this case, because the sum ending on j-1 will definitely be part of the sum ending on j
        and it is the largest sum ending there..
        """

        N = len(nums)
        if N == 1:
            return nums[0]

        dp = [None] * N

        dp[0] = nums[0]

        max_sum = dp[0]

        for i in range(1, N):
            dp[i] = nums[i] + dp[i - 1] if nums[i] + dp[i - 1] > nums[i] else nums[i]
            if dp[i] > max_sum:
                max_sum = dp[i]

        return max_sum


# https://leetcode.com/problems/edit-distance/?envType=problem-list-v2&envId=dynamic-programming
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        I think the question here is:
        - Is this just needleman wunsch?

        The best nw alignment minimizes the levenshtein distance and
        the operations are the definition of exactly that

        Insert: gap in word2
        Delete: gap in word1
        Replace: just normal mismatch

        Ok I think this is identical. Then, let's go about this:

        we only need to return the min ops so no backtracking

        this means we just need the matrix, fill it partially and then compute min(up, diag, left)
        for each cell row by row
        """
        from pprint import pprint

        N = len(word1)
        M = len(word2)

        dp = [[None] * (M + 1) for i in range(N + 1)]

        # top left corner is gap gap and thus 0
        dp[0][0] = 0

        # fill first row left to right
        for i in range(1, M + 1):
            dp[0][i] = i

        # fill first column top to bottom
        for i in range(1, N + 1):
            dp[i][0] = i

        for j in range(1, M + 1):
            for i in range(1, N + 1):
                left = 1 + dp[i][j - 1]
                up = 1 + dp[i - 1][j]
                match = 0 if word1[i - 1] == word2[j - 1] else 1
                diag = dp[i - 1][j - 1] + match
                dp[i][j] = min(left, up, diag)

        return dp[-1][-1]
