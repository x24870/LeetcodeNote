# first try
class Solution:
    def shipWithinDays(self, weights, D):
        l, r = max(weights), sum(weights)
        while l < r:
            mid = (r - l)//2 + l
            day = 1
            load = 0
            for w in weights:
                if (load + w) <= mid:
                    load += w
                else:
                    load = w
                    day += 1
            
            if day > D: # exceed limit days, the ship has to carry more weight
                l = mid + 1
            else:
                r = mid
        return l

weights = [1,2,3,4,5,6,7,8,9,10]
s = Solution()
print(s.shipWithinDays(weights, 5))

# similar to fist solution
class Solution:
    def shipWithinDays(self, weights, D):
        l, r = max(weights), sum(weights)
        while l < r:
            mid = (r - l)//2 + l
            day = 1
            load = 0
            for w in (weights):
                if (load + w) <= mid:
                    load += w
                else:
                    load = w
                    day += 1
                    if day > D:
                        l = mid + 1
                        break
            else:
                r = mid
        return l