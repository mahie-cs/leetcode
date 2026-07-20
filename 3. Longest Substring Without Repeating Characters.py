# Oh this? It's just a medium difficulty question that took me 8 hours to solve.
# I didn't know I can just jump to a different question that is labelled as easy.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        _input = s
        store = []
        snapshot = []
        n = 0
        c = 0
        for i in range(len(_input)):
            cut = _input[i:i+1]
            if cut not in store:
                store.append(cut)
            else:
                snapshot = store.copy()
                del_index = store.index(cut)
                del store[0:del_index+1]
                store.append(cut)
                if c < len(snapshot):
                    c = len(snapshot)
            if len(store) > c:
                c = len(store)
        return c
