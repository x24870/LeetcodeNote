class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alnum = []

        for c in s:
            if c.isalnum(): alnum.append(c)

        mid = len(alnum) // 2
        
        for i in range(mid):
            if alnum[i] != alnum[-i-1]: return False
        return True