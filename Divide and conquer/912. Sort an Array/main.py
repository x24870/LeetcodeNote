class Solution:
    def sortArray(self, nums):
        return sorted(nums)

# Bubble sort
# Will exceed the time limit
class Solution:
    def sortArray(self, nums):
        length = length(nums)
        for i in range(length):
            for j in range(length - i - 1):
                if nums[j] > num[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums

# Selection sort
# Will exceed the time limit
class Solution:
    def sortArray(self, nums):
        length = len(nums)
        for i in range(length - 1):
            # find min in [i:]
            min_idx = i
            for j in range(i+1, length):
                if nums[min_idx] > nums[j]: min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
        return nums

# Insertion sort
# Will exceed the time limit
class Solution:
    def sortArray(self, nums):
        length = len(nums)
        for i in range(1, length):
            position = i
            # insertion
            while position and nums[position] < nums[position-1]:
                nums[position], nums[position-1] = nums[position-1], nums[position]
                position -= 1
        return nums

# Quick sort
# peek **MUST REVIEW**
class Solution:
    def sortArray(self, nums):
        def quick_sort(lo, hi):
            if lo >= hi: return

            key = nums[lo]
            left = lo
            right = hi
 
            while left != right:
                #find the val > key from left
                # while nums[left] < key and right > left: left += 1
                #find the val < key from right
                while nums[right] > key and right > left: right -= 1
                #find the val >= key from left
                while nums[left] <= key and right > left: left += 1
                # if left and right are not meet, change value
                if left < right:
                    nums[left], nums[right] = nums[right], nums[left]

            #change key and meet point
            nums[lo], nums[left] = nums[left], nums[lo]

            #divide to left array and right array by meet point
            quick_sort(lo, left-1)
            quick_sort(left+1, hi)

        quick_sort(0, len(nums)-1)
        return nums

# Heap sort

# Merge sort
# First try
class Solution:
    # according to description, maximun value is 50000
    def sortArray(self, nums):
        INF = 50001
        def merge(l_lo, l_hi, r_lo, r_hi):
            l_idx = 0
            r_idx = 0
            l_arr = nums[l_lo: l_hi+1]
            l_arr.append(INF)
            r_arr = nums[r_lo: r_hi+1]
            r_arr.append(INF)
            for i in range(l_lo, r_hi+1):
                if l_arr[l_idx] < r_arr[r_idx]:
                    nums[i] = l_arr[l_idx]
                    l_idx += 1
                else:
                    nums[i] = r_arr[r_idx]
                    r_idx += 1

        def merge_sort(lo, hi):
            if lo >= hi:
                return
            mid = (hi - lo)//2 + lo
            merge_sort(lo, mid)
            merge_sort(mid+1, hi)
            merge(lo, mid, mid+1, hi)

        merge_sort(0, len(nums)-1)
        return nums

# Shell sort