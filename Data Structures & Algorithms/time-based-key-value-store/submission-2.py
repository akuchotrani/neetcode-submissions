class TimeMap:

    def __init__(self):
        self.myDict = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        val = []
        val.append(value)
        val.append(timestamp)
        if key in self.myDict:
            self.myDict[key].append(val)
        else:
            self.myDict[key] = [val]
        
    def binary_search(self, items, timestamp) -> int:
        if len(items) == 1:
            if items[0][1] <= timestamp:
                return items[0][0]
            else:
                return ""
        left = 0
        right = len(items) - 1
        res = ""
        mid = 0
        while(left <= right):
            mid = (right+left)//2
            print(f"l: {left} r:{right} mid: {mid}")
            if items[mid][1] <= timestamp:
                res = items[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res
                




    def get(self, key: str, timestamp: int) -> str:
        print(f"{self.myDict}")
        if key in self.myDict:
            values = self.myDict[key]
            return self.binary_search(values, timestamp)
        else:
            return ""
        
