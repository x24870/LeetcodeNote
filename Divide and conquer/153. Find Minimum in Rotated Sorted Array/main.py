# First try
class Solution:
    def findMin(self, nums):
        return min(nums)
        
# peek
class Solution:
    def findMin(self, nums):
        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = (hi - lo)//2 + lo
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1

        return nums[lo]