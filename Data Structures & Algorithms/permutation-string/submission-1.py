class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        for s in s1:
            if s in s1_dict:
                s1_dict[s] += 1
            else:
                s1_dict[s] = 1
        
        required_dict = s1_dict.copy()
        start = 0
        end = 0
        for start in range(len(s2)):
            if s2[start] in required_dict:
                end = start
                required_dict = s1_dict.copy()
                while end < len(s2):
                    if s2[end] in required_dict and required_dict[s2[end]] > 0:
                        required_dict[s2[end]] -= 1
                        if required_dict[s2[end]] == 0:
                            del required_dict[s2[end]]
                    else:
                        # print("Resetting the dictionary")
                        required_dict = s1_dict.copy()
                        break
                    
                    if len(required_dict) == 0:
                        # print(f"Required dict is empty at index {end}")
                        # print(f"required_dict : {required_dict}")
                        return True
                    end += 1
                    #print(f"required dict at index {end}: {required_dict}")
        
        return False
                    




        