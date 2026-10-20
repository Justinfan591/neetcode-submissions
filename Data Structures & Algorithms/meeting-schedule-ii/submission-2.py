"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #We just need to know when a meeting starts and we increment the count and move the starting pointer, which ever is the smaller ones, it shows well on the graph
        if len(intervals) == 0: 
            return 0
        starts, ends = [], []
        for interval in intervals: 
            starts.append(interval.start)
            ends.append(interval.end)

        # O(n)
        starts.sort() 
        ends.sort()
        #O(nlogn)
        count = 0
        ans = 0

        s, e = 0,0

        while s < len(starts): 
            if starts[s] < ends[e]: 
                count += 1
                s += 1
                if count > ans:
                    ans = count
            elif starts[s] >= ends[e]: 
                count -= 1
                e += 1
        return ans


