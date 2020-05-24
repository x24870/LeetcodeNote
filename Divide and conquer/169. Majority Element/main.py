from collections import defaultdict

# I peeked into defaultdict() usage
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
