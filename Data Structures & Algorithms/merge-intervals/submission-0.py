class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key = lambda x:x[0])
        print(f"sorted intervals: {intervals}")
        result.append(intervals[0])
        currPtr = 1
        while currPtr < len(intervals):
            # print(f"result: {result}")
            if result[-1][0] <= intervals[currPtr][0] and result[-1][1] >= intervals[currPtr][0]:
                result[-1][1] = max(result[-1][1], intervals[currPtr][1])
            else:
                result.append(intervals[currPtr])
            currPtr += 1
        return result
        