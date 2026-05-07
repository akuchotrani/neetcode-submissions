# 3hr, 5hr, 10hr, 3hr
# 3hr, 3hr same
# 5hr 10hr


7, 4, 1, 0

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        independent_time = []
        for i in range(len(speed)):
            total_distance = target-position[i]
            independent_time.append(total_distance/speed[i])
        # print(f"IndependentTime: {independent_time}")
        pairs = []
        for i in range(len(independent_time)):
            pair = [position[i], independent_time[i]]
            pairs.append(pair)
        # print(f"Unsorted pairs: {pairs}")
        pairs.sort(key = lambda x:x[0])
        # print(f"sorted pairs: {pairs}")

        fleet_counter = 0
        finish_time = 0
        while(len(pairs) > 0):
            top = pairs.pop()
            # print(f"{top[1]}")
            if top[1] > finish_time:
                fleet_counter += 1
                finish_time = top[1]



        return fleet_counter
        