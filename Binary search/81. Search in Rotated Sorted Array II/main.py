class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return target in nums

#peek solution
class Solution:
    def search(self, nums, target):
        if not nums: return False

        l, r = 0, len(nums)-1
        while l <= r:
            mid = (r - l)//2 + l
            if nums[mid] == target:
                return True
            
            while l < mid and nums[l] == nums[mid]: l += 1

            if nums[l] <= nums[mid]: # left is sorted
                if nums[l] <= target < nums[mid]: # use <= because left may contain target when len(left) == 1
                    r = mid - 1
                else:
                    l = mid + 1
            else: # right is sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False

nums = [2,5,6,0,0,1,2]
s = Solution()
print(s.search(nums, 0))