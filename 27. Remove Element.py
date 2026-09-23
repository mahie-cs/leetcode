class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for i in range(len(nums)):
            if val in nums:
                nums.pop(nums.index(val))
        length = len(nums)
        return length
