# My first solution. It took some help form "other" sources for me to solve it.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: List[int] = {}
        for i, n in enumerate(nums):
            leftover = target - n
            if leftover in seen:
                return [seen[leftover], i]
            seen[n] = i
        return []
