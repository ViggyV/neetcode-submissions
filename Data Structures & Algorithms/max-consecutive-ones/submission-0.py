class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        temp = 0
        for i in (nums):
            if(i==1):
                temp+=1
                count = max(temp, count)
            else:
                temp = 0

        return count