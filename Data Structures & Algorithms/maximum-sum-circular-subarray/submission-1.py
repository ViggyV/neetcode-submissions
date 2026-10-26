class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMax,curMin = 0, 0
        globalMax, globalMin = nums[0], nums[0]
        total = 0


        for n in nums:
            curMin = min(curMin + n, n)
            curMax = max(curMax + n, n)

            total += n

            globalMax = max(globalMax, curMax)
            globalMin = min(globalMin, curMin)
        
        if globalMax > 0:
            return max(globalMax, total - globalMin)
        return globalMax