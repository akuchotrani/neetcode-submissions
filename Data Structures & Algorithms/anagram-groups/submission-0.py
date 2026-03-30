class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = {}
        for item in strs:
            item_key = [ 0 for _ in range(26)]
            for alpha in item:
                item_key[ord(alpha) - 97] += 1
            key = str(item_key)
            if key in myDict:
                myDict[key].append(item)
            else:
                myDict[key] = [item]
        
        answer = []
        for key,val in myDict.items():
            answer.append(val)
        return answer

        