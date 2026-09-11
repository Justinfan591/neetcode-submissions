class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #minHeap question
        ans = []
        for num in nums: 
            if len(ans) >= k: 
                temp = heapq.heappop(ans)
                if num > temp: 
                    heapq.heappush(ans, num)
                else: heapq.heappush(ans, temp)
            else: 
                heapq.heappush(ans, num)
        return ans[0]
#no need to pop, can just peek at it 