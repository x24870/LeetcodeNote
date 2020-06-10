# use built-in function
class Solution:
    def search(self, nums, target):
        return nums.index(target) if target in nums else -1

class Solution:
    def search(self, nums, target):
        l = 0
        r = len(nums)
        while l < r:
            mid = (r - l)//2 + l
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1

        return -1