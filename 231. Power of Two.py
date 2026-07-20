class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        product = n
        i = 1
        if product == 1:
            return True
        elif product % 2 != 0 or product <= 0:
            return False
        while product > 0:
            if product ** (1/i) == 2:
                return True
            elif 2 ** i > product:
                return False
            else:
                i += 1
