class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        res = []
        count = 1
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                count += 0
            elif nums[i+1] != nums[i] + 1:
                count = 1
            else:
                count += 1
            res.append(count)
        res.sort()
        n = res[len(res)-1]
        return n