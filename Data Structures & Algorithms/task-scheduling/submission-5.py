class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = []
        dic = {}
        for task in tasks: 
            dic[task] = 1 + dic.get(task,0)
        for value in dic.values(): # we only need the numbers
            maxHeap.append(-value)
        heapq.heapify(maxHeap)
        #now we have a maxHeap
        time = 0
        q = deque() # pairs of [-cnt, idleTime] <- what time to pop back
        while maxHeap or q: 
            time += 1
            

            if maxHeap: 
                cur = heapq.heappop(maxHeap) + 1 
                if cur: 
                    q.append((cur, time + n))
            if q and q[0][1] <= time: 
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

