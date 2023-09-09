class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '-':
                sub = stack.pop()
                stack.append(stack.pop() - sub)
            elif c == '/':
                div = stack.pop()
                stack.append(int(stack.pop() / div))
            else: stack.append(int(c))
        return stack[0]