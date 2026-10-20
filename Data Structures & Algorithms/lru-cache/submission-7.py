class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.q = deque()
        self.dic = {}

    def get(self, key: int) -> int:
        if key not in self.q: 
            return -1
        self.q.remove(key) #n
        self.q.append(key) #1
        return self.dic[key]


    def put(self, key: int, value: int) -> None:
        if key in self.q: 
            self.q.remove(key) #n
            self.q.append(key) #1
            self.dic[key] = value
        else: 
            self.q.append(key)
            self.dic[key] = value
        if len(self.q) > self.size: 
            self.q.popleft() #1