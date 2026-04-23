class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        isNewIntervalAdded = False
        for interval in intervals:
            start = interval[0]
            end = interval[1]

            if end < newInterval[0]:
                result.append(interval)
            elif start > newInterval[1]:
                if isNewIntervalAdded == False:
                    isNewIntervalAdded = True
                    result.append(newInterval)
                result.append(interval)
            else:
                min_start = min(start, newInterval[0])
                max_end = max(end, newInterval[1])
                newInterval[0] = min_start
                newInterval[1] = max_end
        
        if isNewIntervalAdded == False:
            result.append(newInterval)
        print(f"New Interval: {newInterval}")
        return result



        