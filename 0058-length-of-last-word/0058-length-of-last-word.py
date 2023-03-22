class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split()
        j = 0
        for i in l[-1]:
            j += 1
        return j
