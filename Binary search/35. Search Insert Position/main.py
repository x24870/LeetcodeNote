# use built-in function
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) # not len(nums)-1, because the answer may being insert to last index
        
        while l < r:
            m = l + (r - l)//2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m
            else:
                l = m + 1
        return l