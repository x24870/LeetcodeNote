# first try
# exceed time limit and ugly
class TimeMap:
    def __init__(self):
        """
        self_dict =  { 
            key1: { timestamp1: value1, timestamp2: value2 },
            key2: { timestamp1: value1, timestamp2: value2 },
            ...
                      }
        """
        self._dict = {}

    def _get_new_data(self, value, timestamp):
        return {timestamp: value}

    def set(self, key: str, value: str, timestamp: int) -> None:
        key_data = self._dict.get(key)
        if key_data:
            if not key_data.get(timestamp):
                key_data[timestamp] = value
        else:
            self._dict[key] = self._get_new_data(value, timestamp)
        print(self._dict)

    def get(self, key: str, timestamp: int) -> str:
        key_data = self._dict.get(key)
        print("KEY: ", key_data)
        if not key_data:
            return ""
        else:
            ts_lst = list(key_data.keys())
            idx = self._find_upper_bound(ts_lst, timestamp)
            print("idx: ", idx)
            idx -= 1
            return key_data.get(ts_lst[idx])

    def _find_upper_bound(self, lst, target):
        # if target in lst:
            # return target
        l = 0
        r = len(lst)# minus 1 for not exceeding the list range
        print('lst: ', lst, '    target: ', target)
        while l < r:
            mid = (r - l)//2 + l
            print("R:", r, " L:", l, ' M:', mid)
            if lst[mid] > target:
                r = mid
            else:
                l = mid + 1
            print("  R:", r, " L:", l, ' M:', mid)
        return l
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

from collections import defaultdict
class TimeMap:
    def __init__(self):
        """
        self_dict =  { 
            key1: { timestamp1: value1, timestamp2: value2 },
            key2: { timestamp1: value1, timestamp2: value2 },
            ...
                      }
        """
        self._dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._dict[key].append( (value, timestamp) )

    def get(self, key: str, timestamp: int) -> str:
        key_data = self._dict.get(key)
        # print("KEY: ", key_data)
        if not key_data:
            return ""
        else:
            ts_lst = [ data[1] for data in key_data ]
            idx = self._find_upper_bound(ts_lst, timestamp)
            # print("idx: ", idx)
            idx -= 1
            if idx < 0: return ""
            return key_data[idx][0]

    def _find_upper_bound(self, lst, target):
        # if target in lst:
            # return target
        l = 0
        r = len(lst)# minus 1 for not exceeding the list range
        # print('lst: ', lst, '    target: ', target)
        while l < r:
            mid = (r - l)//2 + l
            # print("R:", r, " L:", l, ' M:', mid)
            if lst[mid] > target:
                r = mid
            else:
                l = mid + 1
            # print("  R:", r, " L:", l, ' M:', mid)
        return l