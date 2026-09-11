class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #use heap
        distance = []

        for point in points: 
            x = point[0]
            y = point[1]
            dis = math.sqrt(x*x+y*y)
            heapq.heappush(distance,(dis,x,y))
        ans = []
        for i in range(k): 
            temp = heapq.heappop(distance)
            ans.append([temp[1],temp[2]])
        return ans
