# use python built-in function
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        start_idx = nums.index(target)
        end_idx = start_idx
        max_idx = len(nums)
        while (end_idx+1) < max_idx:
            if nums[end_idx+1] != target:
                break
            end_idx += 1
        return [start_idx, end_idx]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)
        found = -1
        while l < r:
            mid = (r - l)//2 + l
            if nums[mid] == target:
                found = mid
                break

            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        return [-1, -1] if found == -1 else self.search_boundry(target, found, nums)

    def search_boundry(self, target, found, nums):
        max_idx = len(nums) - 1
        start = found
        end = found

        # find start
        while start > 0:
            if nums[start-1] != target:
                break
            start -= 1

        # find end
        while end < max_idx:
            if nums[end+1] != target:
                break
            end += 1

        return [start, end]

# Use upper bound and lower bound
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_start():
            l = 0
            r = len(nums)
            while l < r:
                mid = (r - l)//2 + l
                if nums[mid] >= target:
                    r = mid
                else:
                    l = mid + 1
            # if l == len(num) means target is bigger than all value in nums
            return -1 if l == len(nums) or nums[l] != target else l

        def find_end():
            l = 0
            r = len(nums)
            while l < r:
                mid = (r - l)//2 + l
                if nums[mid] > target:
                    r = mid
                else:
                    l = mid + 1

            # l is upper bound of target, so nums[l-1] is the last value that matching target
            l -= 1
            return -1 if l == -1 or nums[l] != target else l

        return [find_start(), find_end()]