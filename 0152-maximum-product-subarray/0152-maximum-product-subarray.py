class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax, curMin = 1,1 
        res = max(nums)

        for n in nums:
            temp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(temp, n * curMin, n)
            res = max(res, curMax, curMin)
        
        return res