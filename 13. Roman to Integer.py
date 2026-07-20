class Solution:
    def romanToInt(self, s: str) -> int:
        x: dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        result: int = 0
        for i in range(len(s)):
            if i > 0 and x[s[i]] > x[s[i - 1]]:
                result += x[s[i]] - 2 * x[s[i-1]]
            else:
                result += x[s[i]]
        return result
