class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        nums = [-x if i % 2 else x for i, x in enumerate(nums)]
        return sum(nums)


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = defaultdict(int)
        count_frequencies = [[] for i in range(len(nums) + 1)]

        for x in nums:
            num_count[x] += 1

        for x, count in num_count.items():
            count_frequencies[count].append(x)

        res = []
        for i in range(len(count_frequencies) - 1, 0, -1):
            if len(res) >= k:
                return res
            else:
                res.extend(count_frequencies[i])

        return res
