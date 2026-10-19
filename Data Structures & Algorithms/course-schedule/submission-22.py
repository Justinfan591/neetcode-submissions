class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
       #conditions when false: When there appears to be a loop
       #set up a dictionary with start and end
        dic = {}
       # initialize the connections
        for pre in prerequisites: 
            start = pre[0]
            end = pre[1]
            if start not in dic:
                dic[start] = []
            dic[start].append(pre[1])
        #running to give answer
        
        #what if we have it somewhere else? We go through each of it and see if it stops or comes back
        # helper function to check if the current number has a cycle
        visiting = set()
        done = set()
        def has_cycle(curr): 
            if curr in visiting: # base case
                return True
            if curr in done: 
                return False
            visiting.add(curr)
            for nxt in dic.get(curr,[]):
                if has_cycle(nxt): 
                    return True
            visiting.remove(curr) # clean up
            done.add(curr)
            return False
        
        for pre in prerequisites: 
            if has_cycle(pre[0]): 
                return False
        return True






