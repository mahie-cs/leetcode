class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        output: list = [] 
        for i in range(len(nums)):
            if nums[i] not in output:
                output.append(nums[i])
        k = len(output)
        nums[:k] = output
        return k
