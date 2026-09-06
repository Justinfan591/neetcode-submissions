class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = {}
        for course, pre in prerequisites: 
            if course not in dic:
                dic[course] = []
            dic[course].append(pre)
        
        visit = set()
        done = set()
        def dfs(cur): 
            #base case
            if cur in visit: 
                return False
            if cur in done: 
                return True
            if cur not in dic:
                return True
            visit.add(cur)
            for req in dic[cur]:
                if not dfs(req): 
                    return False
            done.add(cur)
            visit.remove(cur)
            return True

        for course in range(numCourses): 
            if not dfs(course):
                return False
        return True
        