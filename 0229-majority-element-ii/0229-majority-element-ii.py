class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        res = []
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, freq in count.items():
            if freq > len(nums)/3:
                res.append(n)
        
        return res
