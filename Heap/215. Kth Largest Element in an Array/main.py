# use built-in sort
# time complexity: O(nlogn)
# space complexity: O(1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]


# use heap
# time complexity: O(nlogk), this method if faster if k is small
# space complexity: O(k)
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for num in nums:
            heapq.heappush(h, num)
            if len(h) > k:
                heapq.heappop(h)

        return h[0]