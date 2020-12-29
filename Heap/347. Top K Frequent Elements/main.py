# time complexity: O(nlogk)
# space complexity: O(n+k)
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            if not d.get(n): d[n] = 1
            else: d[n] += 1
        
        h = []
        for num, count in d.items():
            if len(h) < k:
                heapq.heappush(h, (count, num))
            else:
                heapq.heappushpop(h, (count, num))
        
        return [i[1] for i in h]