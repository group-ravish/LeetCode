class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        for i in range(len(nums)):
            if target == nums[i]:
                index = i
            elif target != nums[i] and target > nums[i]:
                index = i+1
        return index
                
                