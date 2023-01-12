class TimeMap:

    def __init__(self):
        self.hm = collections.defaultdict(list[tuple])
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hm: return ""
        arr = self.hm[key]
        n = len(arr)
        if timestamp >= arr[n-1][0]: return arr[n-1][1]
        if timestamp < arr[0][0]: return ""
        l, r = 0, n-1
        while l < r:
            mid = (l+r) // 2
            if arr[mid][0] <= timestamp:
                l = mid + 1
            else:
                r = mid
        return arr[r-1][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)