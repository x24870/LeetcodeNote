class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windowStart = windowEnd = windowLen = 0
        windowContain = set()
        length = len(s)

        while windowEnd < length:
            if s[windowEnd] not in windowContain:
                windowContain.add(s[windowEnd])
                curLen = windowEnd - windowStart + 1
                if curLen > windowLen: windowLen = curLen
                windowEnd += 1
            else:
                windowContain.remove(s[windowStart])
                windowStart += 1

        return windowLen
