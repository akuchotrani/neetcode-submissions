class Solution:

    def encode(self, strs: List[str]) -> str:
        answer = ""
        for item in strs:
            count = len(item)
            answer += item
            answer += "~"
        print(answer)
        return answer

    def decode(self, s: str) -> List[str]:
        answer = []
        index = 0
        word = ""
        while index != len(s):
            if s[index] == '~':
                answer.append(word)
                word = ""
            else:
                word += s[index]
                # print(f"word: {word}")
            index += 1
        return answer


            
