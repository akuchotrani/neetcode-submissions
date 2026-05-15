class Solution:
    def myPow(self, x: float, n: int) -> float:
        isOdd = False
        if n%2 != 0:
            isOdd = True
        answer = 1
        end = int(n/2)
        for i in range(abs(end)):
            answer *= x
        answer = answer*answer
        if isOdd:
            answer *= x
        if n < 0:
            return 1/answer
        return answer

        