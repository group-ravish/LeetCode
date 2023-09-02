class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = len(nums)*(len(nums)+1)//2
        ar = 0
        for i in nums:
            ar += i
        return(sum - ar)
        