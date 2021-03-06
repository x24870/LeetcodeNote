class Solution:
    def sortArray(self, nums):
        return sorted(nums)

# Bubble sort
# Will exceed the time limit
class Solution:
    def sortArray(self, nums):
        length = len(nums)
        for i in range(length):
            for j in range(length-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums

# Selection sort
# Will exceed the time limit
class Solution:
    def sortArray(self, nums):
        length = len(nums)
        for i in range(length):
            # find min in [i:]
            min_idx = i
            for j in range(i, length):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            nums[min_idx], nums[i] = nums[i], nums[min_idx]
        return nums

# Insertion sort
# Will exceed the time limit
class Solution:
    def sortArray(self, nums):
        for i in range(1, len(nums)):
            pos = i
            # insertion
            while pos and nums[pos] < nums[pos-1]:
                nums[pos], nums[pos-1] = nums[pos-1], nums[pos]
                pos -= 1
        return nums

# Shell sort
# Ref: https://rust-algo.club/sorting/shellsort/index.html
#      http://notepad.yehyeh.net/Content/Algorithm/Sort/Shell/Shell.php
class Solution:
    def sortArray(self, nums):
        MARCIN_GAPS = [701, 301, 132, 57, 23, 10, 4, 1]
        length = len(nums)
        for g in range(len(MARCIN_GAPS)):
            gap = MARCIN_GAPS[g]
            # insertion sort with gap
            for i in range(0, length, gap):
                print(f'i: {i}')
                for j in range(i, 0, -1):
                    cur_idx = j*gap
                    if cur_idx >= length: break
                    pre_idx = (j-1)*gap
                    print(f'cur: {cur_idx}      pre: {pre_idx}')
                    if nums[cur_idx] < nums[pre_idx]:
                        nums[cur_idx], nums[pre_idx] = nums[pre_idx], nums[cur_idx]
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

# my quick sort
class Solution:
    def sortArray(self, nums):
        def quick_sort(lo, hi):
            if lo >= hi: return

            left = lo
            right = hi
            pivot =  nums[lo]
            while right > left:
                while nums[right] > pivot and right > left: right -= 1
                while nums[left] <= pivot and right > left: left += 1
                if right != left:
                    nums[left], nums[right] = nums[right], nums[left]
            
            nums[lo], nums[left] = nums[left], nums[lo]

            quick_sort(lo, left-1)
            quick_sort(left+1, hi)

        quick_sort(0, len(nums)-1)
        return nums

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

# merge sort with out limited max value
class Solution:
    def sortArray(self, nums):
        def merge(l_lo, l_hi, r_lo, r_hi):
            l_idx = 0
            r_idx = 0
            idx = l_lo
            l_arr = nums[l_lo: l_hi+1]
            r_arr = nums[r_lo: r_hi+1]
            l_len = len(l_arr)
            r_len = len(r_arr)
            while r_idx < r_len and l_idx < l_len:
                if l_arr[l_idx] > r_arr[r_idx]:
                    nums[idx] = r_arr[r_idx]
                    r_idx += 1
                else:
                    nums[idx] = l_arr[l_idx]
                    l_idx += 1
                idx += 1
            while l_idx < l_len:
                nums[idx] = l_arr[l_idx]
                l_idx += 1
                idx += 1
            while r_idx < r_len:
                nums[idx] = r_arr[r_idx]
                r_idx += 1
                idx += 1

        def merge_sort(lo, hi):
            if lo >= hi: return
            mid = (hi-lo)//2 + lo
            merge_sort(lo, mid)
            merge_sort(mid+1, hi)
            merge(lo, mid, mid+1, hi)

        merge_sort(0, len(nums)-1)
        return nums

# Heap sort
# peek
class Solution:
    def sortArray(self, nums):
        def heapify(root, length):
            left = root*2 + 1
            right = root*2 + 2
            max_idx = root
            if left < length and nums[left] > nums[root]:
                max_idx = left
            if right < length and nums[right] > nums[max_idx]:
                max_idx = right
            if root != max_idx:
                nums[root], nums[max_idx] = nums[max_idx], nums[root]
                heapify(max_idx, length)

        def heap_sort(nums):
            length = len(nums)
            for i in range(length//2-1, -1, -1):
                heapify(i, length)

            for i in range(length-1, 0, -1):
                nums[0], nums[i] = nums[i], nums[0]
                heapify(0 ,i)

        heap_sort(nums)
        return nums