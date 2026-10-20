class Node: 
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None #placeholder dummy

#least recently used
class LRUCache:
    def __init__(self, capacity: int):
        self.cap =capacity
        self.dic = {}
        #need left and right Nodes
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    #remove the Node
    def remove(self, key): 
        node = self.dic[key]
        prev, nxt = node.prev, node.next
        prev.next = nxt
        node.next.prev = prev

    #insert to the right most 
    def insert(self, key, val): 
        node = Node(key,val)
        last_node = self.right.prev
        node.prev, last_node.next = last_node, node
        node.next, self.right.prev = self.right, node
        self.dic[key] = node

    def get(self, key: int) -> int:
        if key in self.dic: 
            node = self.dic[key]
            self.remove(key)
            self.insert(node.key, node.val) #can be optimized
            return node.val
        else: 
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic: 
            self.remove(key)
            self.insert(key, value)
        else: 
            self.insert(key, value)
        
        if len(self.dic) > self.cap: 
            lru = self.left.next.key
            self.remove(lru)
            del self.dic[lru]




