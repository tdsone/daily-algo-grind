class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        best = 0
        for x in nums_set:
            if x - 1 in nums_set:
                # x cannot be start thus we skip it
                continue

            # x is a sequence head, we increment as long as we find x+1 in the set
            y = 1
            while x + y in nums_set:
                y += 1

            best = max(y, best)

        return best
