class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        array = list(map(int, str(x)))
        reverse_array = array[::-1]
        reverse_num = int("".join(map(str, reverse_array)))
        if x == reverse_num:
            return True
        else:
            return False
