# 1, 2
# 2, 3
# 2, 10
# 4, 5
# 6, 9

# 1, 7
# 5, 6
# 7, 8
# 10, 11
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        result = [intervals[0]]
        counter = 0
        for currPtr in range(1, len(intervals)):
            if result[-1][0] <= intervals[currPtr][0] and result[-1][1] > intervals[currPtr][0]:
                print(f"Collision between {result} and {intervals[currPtr]}")
                counter += 1
                if result[-1][1] >= intervals[currPtr][1]:
                    result[-1][0] = intervals[currPtr][0]
                    result[-1][1] = intervals[currPtr][1]
                    print(f"Updating the result with new interval: {result}")
                else:
                    print(f"Keeping the same result: {result}")
            else:
                result.append(intervals[currPtr])
        print(f"Final result: {result}")
        return counter
        