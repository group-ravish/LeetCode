class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0

        for i in range(len(arr)-1):
            if arr[i] % 2 == 1 and arr[i+1] % 2 == 1:
                count += 1
            else: count = 0
            if count == 2:
                return True
        
        return False
            