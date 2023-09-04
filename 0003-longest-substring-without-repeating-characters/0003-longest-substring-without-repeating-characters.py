class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string = set()
        l = 0
        res = 0
        for i in range(len(s)):
            while s[i] in string:
                string.remove(s[l])
                l += 1
            string.add(s[i])
            res = max(res, len(string))
        return res