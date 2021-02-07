# use python built in 'find()'
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

# brute force
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0

        str_len = len(haystack)
        par_len = len(needle)
        found = False
        idx = 0
        for i in range(str_len - par_len + 1):
            idx = i
            for j in range(par_len):
                if haystack[i+j] != needle[j]:
                    break
                elif j == par_len-1:
                    found = True
            if found: break

        return idx if found else -1

# cleaner brute force
# https://leetcode.com/problems/implement-strstr/discuss/12814/My-answer-by-Python
class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
