class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in string.ascii_lowercase:
            if s.count(i) != t.count(i):
                return False
        return True