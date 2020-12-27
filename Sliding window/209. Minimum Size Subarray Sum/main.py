class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        windowStart = windowEnd = windowSum = windowLen = 0
        length = len(nums)

        for windowEnd in range(length):
            windowSum += nums[windowEnd]

            while windowSum >= s:
                curWindowLen = windowEnd - windowStart + 1
                if windowLen == 0 or curWindowLen < windowLen:
                    windowLen = curWindowLen
                windowSum -= nums[windowStart]
                windowStart += 1

        return windowLen