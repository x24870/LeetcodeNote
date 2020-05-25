# First try
# But return min(nums) is worked too
class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1: return nums[0]
        
        for i in range(length-1):
            if nums[i] > nums[i+1]:
                return nums[i+1]

        return nums[0]


# Without using min()
class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        if length > 2:
            mid = len(nums)//2
            left_min = self.findMin(nums[:mid])
            right_min = self.findMin(nums[mid:])
            return left_min if left_min < right_min else right_min
        elif length == 2:
            return nums[0] if nums[0] < nums[1] else nums[1]
        else:
            return nums[0]

