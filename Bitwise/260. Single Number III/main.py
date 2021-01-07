class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            if not count.get(num):
                count[num] = 1
            else:
                count[num] += 1

        show_once = []
        for key in count.keys():
            if count[key] == 1: show_once.append(key)
        return show_once

# TODO: bitwise solution
# https://blog.techbridge.cc/2020/06/07/leetcode-pattern-bitwise-xor/