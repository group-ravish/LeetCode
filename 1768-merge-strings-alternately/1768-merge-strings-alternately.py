class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        l = 0
        while l < len(word1) and l < len(word2):
            result += word1[l] + word2[l]
            l += 1
        return result + word1[l:] + word2[l:]