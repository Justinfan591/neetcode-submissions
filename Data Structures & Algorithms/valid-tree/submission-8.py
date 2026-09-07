class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Go one direction no loop
        dic = {}
        if edges ==[]:
            return True
        #setting up dependency between nodes
        for A,B in edges: 
            if A not in dic:
                dic[A] = [B]
            else:
                dic[A].append(B)
            if B not in dic: 
                dic[B] = [A]
            else:
                dic[B].append(A)
        visit = set()

        def dfs(cur, parent):
            #base case: nothing else to go down with
            #have parent so it knows what not to consider loop
            if cur in visit: 
                return False
            visit.add(cur)

            for nxt in dic[cur]: 
                if nxt == parent: 
                    continue # skip if it is parent
                if not dfs(nxt, cur): 
                    return False
            return True 
        if not dfs(0, -1):
            return False #-1 as indication of no parent as a placeholder
        if len(visit) == n:
            return True
        else: return False
        