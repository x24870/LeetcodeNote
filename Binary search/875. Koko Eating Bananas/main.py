# first try
class Solution:
    def minEatingSpeed(self, piles, H):
        l, r = 1, max(piles)+1
        min_k = 10**9 # according to description, piles[i] max value is 10^9
        while l < r:
            mid = (r - l)//2 + l
            count = 0
            eat_all = True
            for p in piles:
                count += p//mid
                if p%mid: count += 1
                if count > H: # exceed limit time
                    eat_all = False
                    break 

            if eat_all and min_k > mid: min_k = mid
            # print("eat_all: {},   mid: {}".format(eat_all, mid))
            if eat_all: # means koko can eat slower
                r = mid
            else: # means koko have to eat faster
                l = mid + 1

        return min_k



piles = [30,11,23,4,20]
s = Solution()
ans = s.minEatingSpeed(piles, 5)
print(ans)

# This solution is more clear
class Solution2:
    def minEatingSpeed(self, piles, H):
        l, r = 1, max(piles)+1
        while l < r:
            mid = (r - l)//2 + l
            count = 0
            for p in piles:
                count += p//mid
                if p%mid: count += 1
            if count <= H:
                r = mid
            else:
                l = mid + 1
        return l

piles = [30,11,23,4,20]
s = Solution2()
ans = s.minEatingSpeed(piles, 5)
print(ans)