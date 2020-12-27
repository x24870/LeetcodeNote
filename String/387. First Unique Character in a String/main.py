# first try
class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict = {}
        for c in s:
            if not char_dict.get(c):
                char_dict[c] = 1
            else:
                char_dict[c] += 1
        for i in range(len(s)):
            if char_dict[s[i]] == 1: return i
        # not found
        return -1