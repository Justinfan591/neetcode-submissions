class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return None
        
        old_to_new = {}

        def dfs(cur):
            if cur in old_to_new: 
                return old_to_new[cur]
            
            clone = Node(cur.val)
            old_to_new[cur] = clone
            for nei in cur.neighbors: 
                clone.neighbors.append(dfs(nei))
                
            return clone
        return dfs(node)