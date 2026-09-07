class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #similar to island
        #setting up the connections
        dic = {} 
        for A,B in edges: 
            if A not in dic: 
                dic[A] = [B]
            else: 
                dic[A].append(B)
            if B not in dic: 
                dic[B] = [A]
            else: 
                dic[B].append(A)
        def dfs(i):
            #base case
            if i in visit: 
                return 
            visit.add(i)
            for nei in dic.get(i,[]): 
                dfs(nei)
            return 


        visit = set()
        chunks = 0
        for i in range(n): 
            if i not in visit: 
                chunks += 1
                dfs(i)
        return chunks