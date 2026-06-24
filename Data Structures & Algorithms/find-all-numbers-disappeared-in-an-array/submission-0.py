class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        n  = len(nums)
        hash = set(range(1,n+1))

        for num in nums:
            hash.discard(num)

        return list(hash) 