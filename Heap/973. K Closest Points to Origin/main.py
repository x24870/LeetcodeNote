import heapq
from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        h = []
        for p in points:
            # heapq is min-heap, but we want to find closest K points
            # so we have to use max-heap
            # The easiest way is turn the distance to minus
            # then the heap root will be the max distance
            if len(h) < K:
                heapq.heappush(h, [-sqrt(p[0]**2 + p[1]**2), p])
            else:
                heapq.heappushpop(h, [-sqrt(p[0]**2 + p[1]**2), p])

        return [x[1] for x in h]