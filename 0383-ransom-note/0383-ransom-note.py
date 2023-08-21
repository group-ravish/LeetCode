class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # ransom = {}
        # mag = {}

        # for i in range(len(ransomNote)):
        #     ransom[ransomNote[i]] = 1 + ransom.get(ransomNote[i], 0)

        # for i in range(len(magazine)):
        #     mag[magazine[i]] = 1 + mag.get(magazine[i], 0)

        # print(ransom)
        # print(mag)
        # if ransom.items() <= mag.items():
        #     return True
        # return False
        for i in ransomNote:
            print(i)
            if magazine.count(i) >= ransomNote.count(i):
                continue
            else: return False
        return True