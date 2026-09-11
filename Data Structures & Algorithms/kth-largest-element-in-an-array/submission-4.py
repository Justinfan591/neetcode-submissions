class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []  # min heap of the k largest seen so far
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif num > heap[0]:              # peek, O(1)
                heapq.heapreplace(heap, num) # pop min + push, one O(log k) op
        return heap[0]                       # peek, no need to pop