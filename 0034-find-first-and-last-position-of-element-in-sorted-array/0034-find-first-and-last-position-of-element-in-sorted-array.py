class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l+r)//2
                if target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            return [l, r]

        left = binarySearch(nums,target-0.1)
        right = binarySearch(nums,target+0.1)
        
        if left[0]!=right[0]:
            return[left[0],right[1]]

        return [-1,-1]