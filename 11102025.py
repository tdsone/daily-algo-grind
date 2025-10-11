class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        nums = [-x if i % 2 else x for i, x in enumerate(nums)]
        return sum(nums)
