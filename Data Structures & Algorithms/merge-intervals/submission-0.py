class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort by start time
        ordered = sorted(intervals, key = lambda l:l[0])
        ans = []

        start = ordered[0][0]
        end = ordered[0][1]

        for interval in ordered: 
            curr_start = interval[0]
            curr_end = interval[1]
            if curr_start > end: 
                ans.append([start,end])
                start = curr_start
                end = curr_end
            elif curr_end > end: 
                end = curr_end
        ans.append([start,end])
        return ans

