class MinStack:

    def __init__(self):
        self.my_stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.my_stack.append(val)
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            top = self.min_stack[-1]
            minimum_val = min(top, val)
            self.min_stack.append(minimum_val)


    def pop(self) -> None:
        if len(self.my_stack) > 0:
            self.my_stack.pop()
            self.min_stack.pop()

    def top(self) -> int:
        return self.my_stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
