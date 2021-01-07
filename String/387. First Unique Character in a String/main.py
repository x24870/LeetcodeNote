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

from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        def return_zero():
            return 0

        char_dic = defaultdict(return_zero)

        for c in s:
            char_dic[c] += 1

        char_lst = list(s)
        for i in range(len(char_lst)):
            if char_dic[char_lst[i]]: return i

        return -1

# use defaultdict
# slightly faster
from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        def return_zero():
            return 0

        char_dic = defaultdict(return_zero)

        for c in s:
            char_dic[c] += 1

        char_lst = list(s)
        for i in range(len(char_lst)):
            if char_dic[char_lst[i]] == 1: return i

        return -1