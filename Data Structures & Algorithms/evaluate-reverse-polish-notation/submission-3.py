class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_stack = []

        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                my_stack.append(int(token))
            else:
                if token == '+':
                    first = my_stack.pop()
                    second = my_stack.pop()
                    res = first + second
                    my_stack.append(res)
                elif token == '-':
                    first = my_stack.pop()
                    second = my_stack.pop()
                    res = second - first
                    my_stack.append(res)
                elif token == '/':
                    first = my_stack.pop()
                    second = my_stack.pop()
                    res = int(second / first)
                    my_stack.append(res)
                elif token == '*':
                    first = my_stack.pop()
                    second = my_stack.pop()
                    res = first * second
                    my_stack.append(res)
        
        return my_stack.pop()
        