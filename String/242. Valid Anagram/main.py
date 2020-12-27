# first try
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for c in s:
            if not s_dict.get(c):
                s_dict[c] = 1
            else:
                s_dict[c] += 1

        for c in t:
            if not t_dict.get(c):
                t_dict[c] = 1
            else:
                t_dict[c] += 1

        s_keys = s_dict.keys()
        t_keys = t_dict.keys()

        if s_keys != t_keys: return False
        for key in s_keys:
            if s_dict[key] != t_dict[key]: return False
        
        return True


# check the appear times of each charactor
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chr = [0] * 26
        t_chr = [0] * 26

        for c in s:
            s_chr[ord(c) - ord('a')] += 1

        for c in t:
            t_chr[ord(c) - ord('a')] += 1

        for idx, val in enumerate(s_chr):
            if val != t_chr[idx]: return False
        return True