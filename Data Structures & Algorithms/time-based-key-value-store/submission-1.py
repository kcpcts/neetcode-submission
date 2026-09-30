class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        
        vals = self.store[key]
        if not vals:
            return ""
        if vals[0][0] > timestamp:
            return ""
        
        left = 0
        right = len(vals)-1
        while left <= right:
            mid = (left + right) // 2
            if vals[mid][0] > timestamp:
                right = mid - 1
            if vals[mid][0] < timestamp:
                left = mid + 1
            if vals[mid][0] == timestamp:
                return vals[mid][1]
        
        return vals[right][1]
