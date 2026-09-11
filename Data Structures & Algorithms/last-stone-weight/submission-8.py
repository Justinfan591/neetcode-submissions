class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while(len(stones) > 1): 
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if first < second: #right now it is negative so first 
                heapq.heappush(stones, first - second)
        
        return -heapq.heappop(stones) if stones else 0