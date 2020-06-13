# peek
# Binary search
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = (r - l)//2 + l
            mid_square = mid**2
            if mid_square == x:
                return mid
            
            if mid_square > x:
                r = mid - 1
            else:
                l = mid + 1
        return r