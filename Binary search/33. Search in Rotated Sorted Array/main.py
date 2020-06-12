class Solution:
    def search(self, nums, target):
        def find_min_idx(nums):
            l = 0
            r = len(nums) - 1
            while l < r:
                mid = (r - l)//2 + l
                if nums[mid] < nums[r]:
                    r = mid
                else:
                    l = mid + 1
            return l

        def find_target_idx(nums, l, r, target):
            while l < r:
                mid = (r - l)//2 + l
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid
                else:
                    l = mid + 1
            return -1

        pivot = find_min_idx(nums)
        l_result = find_target_idx(nums, 0, pivot, target)
        r_result = find_target_idx(nums, pivot, len(nums), target)

        if l_result == -1 and r_result == -1: return -1
        return l_result if r_result == -1 else r_result

