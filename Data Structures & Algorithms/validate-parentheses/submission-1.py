class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []

        for bracket in s:
            if bracket == '(' or bracket == '[' or bracket == '{':
                my_stack.append(bracket)
            elif bracket == ')':
                if len(my_stack) != 0 and my_stack[-1] == '(':
                    my_stack.pop()
                else:
                    return False
            elif bracket == '}':
                if len(my_stack) != 0 and my_stack[-1] == '{':
                    my_stack.pop()
                else:
                    return False
            elif bracket == ']':
                if len(my_stack) != 0 and my_stack[-1] == '[':
                    my_stack.pop()
                else:
                    return False
        if len(my_stack) != 0:
            return False
        return True