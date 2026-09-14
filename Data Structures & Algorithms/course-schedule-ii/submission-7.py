class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #output is different: returns the order of courses that should be taken
        ans = []
        dic = defaultdict(list)
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
            visit.add(cur)
            for req in dic[cur]:
                if not dfs(req): 
                    return False
            visit.remove(cur) #to mean "on my current path"
            done.add(cur)
            ans.append(cur) 
            return True

        for course in range(numCourses): 
            if not dfs(course):
                return []
        return ans
