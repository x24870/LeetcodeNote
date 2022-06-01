package main

// time complexity: O(logN)
// space complexity: O(1)
func peakIndexInMountainArrayBinSearch(arr []int) int {
	l, r := 0, len(arr)-1
	mid := 0

	for l < r {
		mid = l + (r-l)/2
		if arr[mid-1] < arr[mid] && arr[mid] > arr[mid+1] {
			return mid
		} else if arr[mid-1] < arr[mid] {
			l = mid
		} else {
			r = mid
		}
	}

	return mid
}

// time complexity: O(n)
// space complexity: O(1)
func peakIndexInMountainArray(arr []int) int {
	peak := 0
	for peak < len(arr) {
		if arr[peak] > arr[peak+1] {
			break
		}
		peak++
	}

	return peak
}
