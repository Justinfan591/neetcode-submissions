class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = {}
        #initialize dependency 
        for pre in prerequisites: 
            if pre[0] in dic: 
                dic[pre[0]].append(pre[1])
            else: dic[pre[0]] = [pre[1]] # this is a list because one node/point can be linked to many other nodes
        visiting, done = set(), set()
        
        def has_cycle(start): 
            if start in done: 
                return False
            if start in visiting: 
                return True
            
            if start in dic: 
                visiting.add(start)
                for nxt in dic[start]: 
                    if has_cycle(nxt): 
                        return True # only return False at the end
                visiting.remove(start)
            done.add(start)
            return False
        
        for i in range(numCourses): 
            if has_cycle(i): 
                return False
            else: 
                done.add(i)
        return True
            
            







