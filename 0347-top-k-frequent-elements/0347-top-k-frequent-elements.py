class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        input = [[] for i in range(len(nums) + 1)]
        for i in nums:
            count[i] = 1 + count.get(i, 0)
        for i, freq in count.items():
            input[freq].append(i)
        
        res = []
        for i in range(len(input)-1, 0, -1):
            for j in input[i]:
                res.append(j)
                if len(res) == k:
                    return res
        