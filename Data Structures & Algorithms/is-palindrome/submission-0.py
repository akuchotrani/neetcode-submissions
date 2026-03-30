class Solution:
    def pre_process(self, s: str) -> str:
        cleaned_s = "".join(char.lower() for char in s if char.isalnum())
        return cleaned_s

    def isPalindrome(self, s: str) -> bool:
        
        user_input = self.pre_process(s)
        start = 0
        end = len(user_input) - 1
        print(f"start: {start} and end: {end}")
        while(start < end):
            print(f"checking start: {user_input[start]} and end:{user_input[end]}")
            if(user_input[start] != user_input[end]):
                return False
            else:
                start += 1
                end -= 1
        
        return True
        