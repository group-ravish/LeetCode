class Solution:
    def isValid(self, s: str) -> bool:
        stack = [0]
        bracket = {
            0: None, 
            '(':')', 
            '[':']', 
            '{':'}'
        }
        for i in s:
            if i in bracket: 
                stack.append(i)
            else:
                if bracket[stack.pop()] != i: return False
        return stack == [0]