class TimeMap:

    def __init__(self):
        self.dict = {} 
        #key is the key
        #value is [value, timestamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []
        self.dict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        #initialize res
        res = ''
        #get the value(list of [value, timestamp]) of the dict
        #if there is no key, return []
        valueList = self.dict.get(key,[])
        #after get the list, use binary search because timestamp is increasing
        #to search for the value in [value, timestamp] that is less than or equal to timestamp
        left = 0
        right = len(valueList) - 1
        while left <= right:
            mid = (left+right)//2
            if valueList[mid][1] <= timestamp:
                #[[bar,3],[bar,5]] timestamp = 2
                res = valueList[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)