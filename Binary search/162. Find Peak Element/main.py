# first try
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        
        for i in range(1, len(nums)-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
            
        if nums[0] > nums[1]: return 0
        
        max_idx = len(nums) - 1
        if nums[max_idx] > nums[max_idx-1]: return max_idx # here can just return max_idx

# Linear scan - divide the problem into 3 cases
# 1. The list is ascending (last is peak)
# 2. The list is descending (first is peak)
# 3. There is a peak
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # This loop will go through the list items but last one
        # if len(nums) == 1, this loop will not run
        # So I deal with these two exception at last line
        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]:
                return i
        return 0 if len(nums) == 1 else len(nums)-1

# Binary search - recursive
# Select mid and compare to mid+1
# If mid < mid+1, which means the peak will appear at right sub-array
# Otherwisem, the peak will appear at left sub-array
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def bin_search_peak(l, r):
            if l == r: return l
            mid = (r - l)//2 + l
            if nums[mid] < nums[mid+1]:
                return bin_search_peak(mid+1, r)
            else:
                return bin_search_peak(l, mid)

        return bin_search_peak(0, len(nums)-1)

# Binary search - iterative
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l != r:
            mid = (r - l)//2 + l
            if nums[mid] < nums[mid+1]:
                l = mid + 1
            else:
                r = mid
        return l