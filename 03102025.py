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
