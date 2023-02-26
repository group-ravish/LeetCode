class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        x = 0
        while i < len(nums):
            if(nums[i] == 0):
                len(nums) == len(nums)-1
                del nums[i]
                x = x+1 
            else: i = i+1               
        nums.extend([0] * x)
        
