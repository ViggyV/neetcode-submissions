class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = set()

        for i, n in enumerate(nums):
            if n in numSet:
                return True
            numSet.add(n)
        return False