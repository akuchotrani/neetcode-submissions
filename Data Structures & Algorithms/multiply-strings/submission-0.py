class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        x = 0
        for char in num1:
            x = x*10 + int(char)
        
        y = 0
        for char in num2:
            y = y*10 + int(char)
        
        return str(x*y)
        