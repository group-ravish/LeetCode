class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1
        while lp <= rp:
            mid = (lp + rp)//2
            if target > nums[mid]:
                lp = mid+1
            elif target < nums[mid]: 
                rp = mid-1
            else:
                return mid
        return -1