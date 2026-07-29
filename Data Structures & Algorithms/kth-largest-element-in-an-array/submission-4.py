class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-x for x in nums]
        heapq.heapify(heap)

        for i in range(k):
            n = heapq.heappop(heap)
            if i + 1 == k:
                return -n