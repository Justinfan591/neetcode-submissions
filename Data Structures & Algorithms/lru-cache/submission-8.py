class Node: 
    def __init__(self, key, val): 
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dic = {}

        #left = LRU right = most recent
        self.left, self.right = Node(0,0), Node(0,0) #dummy
        self.left.next, self.right.prev = self.right, self.left

    #remove LRU can be in the middle
    def remove(self, node): 
        nxt, prev = node.next, node.prev
        prev.next = nxt
        nxt.prev = prev

    #insert to the right
    def insert(self, node): 
        node.next = self.right
        node.prev = self.right.prev
        self.right.prev.next = node
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.dic: 
            node = self.dic[key]
            self.remove(node)
            self.insert(node)
            return node.val #dic[key] is a node 
        else: return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic: 
            node = self.dic[key]
            self.remove(node)
            new_node = Node(key,value)
            self.insert(new_node)
            self.dic[key] = new_node
        else: # not in dic
            new_node = Node(key, value)
            self.insert(new_node)
            self.dic[key] = new_node
            if len(self.dic) > self.cap:
                lru = self.left.next
                self.remove(lru)
                del self.dic[lru.key] 
            
            

