class Solution:
    def climbStairs(self, n: int) -> int:
        first, last = 1, 1
        for i in range(1, n):
            first, last = first + last, first
        return first
