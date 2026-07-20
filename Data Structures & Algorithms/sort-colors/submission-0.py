class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0, 0, 0]

        for i in nums:
            colors[i] += 1


        i = 0
        for color in range(len(colors)):
            for j in range(colors[color]):
                nums[i] = color
                i += 1
        
        return nums