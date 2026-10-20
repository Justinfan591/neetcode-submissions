"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #sort based on start O(nlogn)
        ordered = sorted(intervals, key = lambda x: x.start)
        #initiation
        if len(ordered) == 0 :
            return True

        start = ordered[0].start
        end = ordered[0].end

        for i in range(1,len(ordered)):
            interval = ordered[i]
            
            curr_start = interval.start
            curr_end = interval.end

            if curr_start < end: 
                return False
            end = curr_end
        return True
