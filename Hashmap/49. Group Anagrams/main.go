package main

import (
	"sort"
	"strings"
)

// n = len(strs), m = len(strs[0])
// time complexity: O(mlogm*n)
// space complexity: O(n*m)
func groupAnagrams(strs []string) [][]string {
	ans := make(map[string][]string)
	for _, s := range strs {
		sorted := sortString(s)
		ans[sorted] = append(ans[sorted], s)
	}

	ret := [][]string{}
	for _, v := range ans {
		ret = append(ret, v)
	}
	return ret
}

func sortString(s string) string {
	strs := strings.Split(s, "")
	sort.Strings(strs)
	return strings.Join(strs, "")
}
