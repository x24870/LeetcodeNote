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
            ts_lst = list(key_data.keys()) # Cost too many time
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
            key1: [ (timestamp1: value1), (timestamp2: value2) ],
            key2: [ (timestamp1: value1), (timestamp2: value2) ],
            ...
                      }
        """
        self._dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._dict[key].append( (timestamp, value) )

    def get(self, key: str, timestamp: int) -> str:
        key_data = self._dict.get(key)
        if not key_data:
            return ""
        else:
            idx = self._find_upper_bound(key_data, timestamp)
            return "" if idx == 0 else key_data[idx-1][1]

    def _find_upper_bound(self, key_data, target):
        '''
        key_data format: [ (timestamp1: value1), (timestamp2: value2) ]
        '''
        l = 0
        r = len(key_data)# minus 1 for not exceeding the list range
        while l < r:
            mid = (r - l)//2 + l
            if key_data[mid][0] > target:
                r = mid
            else:
                l = mid + 1
        return l


# Use python built-in bisect module
import bisect
class TimeMap:
    def __init__(self):
        """
        self_dict =  { 
            key1: [ (timestamp1: value1), (timestamp2: value2) ],
            key2: [ (timestamp1: value1), (timestamp2: value2) ],
            ...
                      }
        """
        self._dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._dict[key].append( (timestamp, value) )

    def get(self, key: str, timestamp: int) -> str:
        key_data = self._dict.get(key)
        if not key_data:
            return ""
        else:
            idx = bisect.bisect( key_data, (timestamp, chr(127)) )
            return "" if idx == 0 else key_data[idx-1][1]

        '''
        jcodem explained about chr(127)

        i = bisect.bisect(a,b) will set i to the first index where a[i] > b
        for this case- a is our list of tuples and b is our target tuple
        to correctly define the target we must provide a tuple following format (number, string).
        number is timestamp. string we must use a value > any provided string.
        i.e. 'z' > 'yyyyy', therefore 'z'+1 must be greater than any 'a-z' string.
        chr( ord('z')+1 ) = chr(123)
        chr(127) can also be used to include all valid ascii characters(7 bits 0-127)
        '''