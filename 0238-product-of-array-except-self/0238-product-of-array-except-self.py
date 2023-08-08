class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        res = [0] * n
        
        lp = 1
        for i in range(n):
            left[i] = lp
            lp *= nums[i]

        rp = 1
        for i in range(n-1, -1, -1):
            right[i] = rp
            rp *= nums[i]
        
        for i in range(n):
            res[i] = left[i] * right[i]
        return res