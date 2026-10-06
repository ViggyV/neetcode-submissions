class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if not nums:
            return 0

        l = len(nums)
        res = nums[0]
        curr = nums[0]

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                curr += nums[i]
                res = max(curr, res)
            else:
                curr = nums[i]
            
        return res
