class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)):
            if (digits[-1] == 9):
                digit = int("".join(map(str, digits)))
                digit += 1
                digits = [int(x) for x in str(digit)]
                break
            else:    
                digits[-1] += 1
                break
        return digits