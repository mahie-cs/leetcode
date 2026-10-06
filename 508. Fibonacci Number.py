class Solution:
    def fib(self, n: int) -> int:
        a: int = 0
        b: int = 1
        j: int = 0
        if n == 1:
            return 1
        for i in range(1, n):
            j = a + b
            a = b
            b = j
        return j
