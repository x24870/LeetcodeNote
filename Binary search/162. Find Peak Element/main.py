class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        
        for i in range(1, len(nums)-1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i
            
        if nums[0] > nums[1]: return 0
        
        max_idx = len(nums) - 1
        if nums[max_idx] > nums[max_idx-1]: return max_idx