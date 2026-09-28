class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        j: int = 0
        k: int = 0
        lps: list[int] = [0]
        for i in range(1, len(needle)):
            while j > 0 and needle[i] != needle[j]:
                j = lps[j-1]
            if needle[i] == needle[j]:
                j += 1
            lps.append(j)
        
        for h in range(len(haystack)):
            while k > 0 and haystack[h] != needle[k]:
                k = lps[k-1]
            if haystack[h] == needle[k]:
                k += 1
            if k == len(needle):
                return h-k+1
        return -1
