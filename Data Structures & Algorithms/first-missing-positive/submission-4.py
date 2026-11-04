class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        count = 1
        while(count in nums):
            count += 1
        return count
    
    