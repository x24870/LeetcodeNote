# First try
# faster than binary search
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for i in range(1, len(A)-1):
            if A[i-1] < A[i] > A[i+1]:
                return i


# Binary search
# Select a mid, then prune the side that smaller than the mid
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l, r = 0, len(A)-1
        while l < r:
            mid = (r - l)//2 + l
            if A[mid] > A[mid+1]:
                r = mid
            else:
                l = mid + 1
        return l