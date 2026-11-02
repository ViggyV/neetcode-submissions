class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        L = 0
        total = 0
        res = 0

        for r in range(len(arr)):
            total += arr[r]
            if r - L + 1 > k:
                total -= arr[L]
                L += 1
            if (r - L + 1) == k and total / k >= threshold:
                res += 1
        return res