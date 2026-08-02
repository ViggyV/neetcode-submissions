class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        nums = []

        def backtrack(i, nums):
            if len(nums) == k:
                res.append(nums.copy())
                return 
            
            for i in range(i, n+1):
                nums.append(i)
                backtrack(i+1, nums)
                nums.pop()

        backtrack(1, [])
        return res
