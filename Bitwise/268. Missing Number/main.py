class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for i in range(len(nums) + 1):
            if i not in nums_set:
                return i

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        bitwise = 0
        for i in range(length+1):
            bitwise ^= i
        for num in nums:
            bitwise ^= num
        return bitwise

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        # first parentheses is last_num:len(nums) + first_num:0
        # second parentheses is the true length of nums
        correct_sum = (length) * (length+1) // 2
        return correct_sum - sum(nums)