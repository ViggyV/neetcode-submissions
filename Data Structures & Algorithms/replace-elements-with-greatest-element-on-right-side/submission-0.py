class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        k = len(arr) -2
        max = arr[-1]
        arr[-1] = -1

        while(k >= 0):
            temp = arr[k]
            arr[k] = max
            if temp > max:
                max = temp      
            k -= 1
        return arr

