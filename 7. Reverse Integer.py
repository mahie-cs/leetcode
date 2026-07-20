class Solution:
    def reverse(self, x: int) -> int:
        temp = ""
        _int = 0
        if x < 0:
            x *= -1
            temp = str(x)[::-1]
            _int = (-1) * int(temp)
        else:
            temp = str(x)[::-1]
            _int = int(temp)

        if _int < -2147483648 or _int > 2147483647 - 1:
            return 0
        return _int
