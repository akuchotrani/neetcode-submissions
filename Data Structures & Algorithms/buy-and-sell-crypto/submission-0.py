class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1

        if len(prices) <= 1:
            return 0
        
        answer = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                answer = max(answer, prices[right] - prices[left])
            else:
                left = right
            right += 1
        return answer




        