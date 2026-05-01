class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monotonicStack = []
        indexStack = []
        result = [0 for _ in range(len(temperatures))]
        for i in range(len(temperatures)):
            if len(monotonicStack) == 0 or monotonicStack[-1] > temperatures[i]:
                monotonicStack.append(temperatures[i])
                indexStack.append(i)
            else:
                while monotonicStack and monotonicStack[-1] < temperatures[i]:
                    index = indexStack.pop()
                    result[index] = i - index
                    monotonicStack.pop()
                monotonicStack.append(temperatures[i])
                indexStack.append(i)
        return result 
        