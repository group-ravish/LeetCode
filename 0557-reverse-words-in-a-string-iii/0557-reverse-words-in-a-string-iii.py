class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(map(lambda r: r[::-1], s.split()))
