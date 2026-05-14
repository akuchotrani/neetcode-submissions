class Solution:
    def findRemainingTasks(self, taskDict):
        taskRemaining = []
        sortedTasks = sorted(taskDict.items(), key=lambda x: x[1], reverse=True)
        for key,val in sortedTasks:
            if val >= 1:
                taskRemaining.append(key)
        return taskRemaining

    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Create a dictionary of task with count
        # For every cpu cycle
            # 1) Try to evict any task which is completed
            # 2) Allocate a new task
                # 2a) Check if a task is not in CPU allocate
                # 2b) If no task found just sit idle for next cpu cycle
        
        taskDict = {}
        for task in tasks:
            if task not in taskDict:
                taskDict[task] = 1
            else:
                taskDict[task] += 1
        # print(f"Task Dict: {taskDict}")

        cpuHeap = []
        cpuCycleCount = 0

        while len(self.findRemainingTasks(taskDict)) > 0:
            # print(f"cpuHeap: {cpuHeap} remainingTasks: {self.findRemainingTasks(taskDict)}")
            if len(cpuHeap) > 0 and cpuHeap[0][0] <= cpuCycleCount:
                heapq.heappop(cpuHeap)
            for task in self.findRemainingTasks(taskDict):
                if task not in [item[1] for item in cpuHeap]:
                    heapq.heappush(cpuHeap,(cpuCycleCount+n+1, task))
                    taskDict[task] -= 1
                    break
            cpuCycleCount +=1
        # print(f"Final CPU Heap: {cpuHeap}")
        return cpuCycleCount
        

        