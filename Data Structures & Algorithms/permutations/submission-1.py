class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, nums):
            if not nums:
                res.append(path)
                return 

            for i in range(len(nums)):
                backtrack(path + [nums[i]], nums[:i] + nums[i+1:])
        
        res = []
        backtrack([], nums)
        return res