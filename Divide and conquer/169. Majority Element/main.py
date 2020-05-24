from collections import defaultdict, Counter
import random

# I peeked into defaultdict() usage
# First try
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        appeared_num = defaultdict(self.return_zero)
        for i in nums:
            appeared_num[i] += 1

        return max(appeared_num, key=appeared_num.get)
        # above line equals to:
        # inverse = [(val, key) for key, val in appeared_num.items()]
        # return max(inverse)[1]

    def return_zero(self):
        return 0

# Counter is a subclass of dictionary
class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        # most_common(1) return a list contains the sets of most common elements
        # [(key, count)]
        return counts.most_common(1)[0][1]

# Sorting the list, because the count of majority must > n/2
# so the majority number must at middle of a sorted list
class Solution:
    def majorityElement(self, nums):
        nums.sort()
        return nums[len(nums)//2]

# It is technically possible for this algorithm to run indefinitely if we never manage to randomly select the majority element 
# so the worst possible runtime is unbounded.
# But the majority element is guaranteed to occupy more than half of the array, so the expected runtime is far better 
class Solution:
    def majorityElement(self, nums):
        majority_counts = len(nums)//2
        while True:
            candidate = random.choice(nums)
            if sum(1 for num in nums if num == candidate) > majority_counts:
                return candidate

# divide and conquer solution
class Solution:
    def majorityElement(self, nums):
        def find_majority_recursive(lo, hi):
            if lo == hi:
                return nums[lo]

            mid = (hi - lo)//2 + lo
            left_majority = find_majority_recursive(lo, mid)
            right_majority = find_majority_recursive(mid+1, hi)

            if left_majority == right_majority:
                return left_majority

            left_count = sum( 1 for i in range(lo, hi+1) if nums[i] == left_majority )
            right_count = sum( 1 for i in range(lo, hi+1) if nums[i] == right_majority )
            return left_majority if left_count > right_count else right_majority

        return find_majority_recursive(0, len(nums)-1)

# Boyer-Moore Voting Algorithm
# First try
class Solution:
    def majorityElement(self, nums):
        candidate = nums[0]
        vote = 1

        for i in range(1, len(nums)):
            if candidate == nums[i]:
                vote += 1
            else:
                vote -= 1
                if vote == 0:
                    candidate = nums[i]
                    vote = 1

        return candidate

# Boyer-Moore Voting Algorithm2
class Solution:
    def majorityElement(self, nums):
        candidate = None
        vote = 0

        for num in nums:
            if vote == 0:
                candidate = num
            vote += (1 if candidate == num else -1)
            
        return candidate
