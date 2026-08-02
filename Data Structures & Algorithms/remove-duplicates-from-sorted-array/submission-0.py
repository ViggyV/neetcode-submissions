class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = r = 0
        size = len(nums)

        while r < size:
            nums[l] = nums[r]
            while r < size and nums[r] == nums[l]:
                r += 1
            l += 1
        return l
