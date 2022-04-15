class LRUCache:
    
    def __init__(self, capacity):
        self.capacity = capacity
        print('self.capacity ', self.capacity)
        self. dict = {}
        print('self.dict ', self.dict)
        
    def get(self, key):
        print('key ', key)
        print('self.dict di get ', self.dict)

        if key not in self.dict:
            return -1
        val = self.dict[key]
        del self.dict[key]
        self.dict[key] = val
        print('self.dict di get before return ', self.dict)

        return val

    def put(self, key, value):
        print('key ', key)
        print('value ', value)
        print('self.dict di put ', self.dict)

        if key in self.dict:
            del self.dict[key]

        print('self.dict di put after del dict[key]', self.dict)
        
        self.dict[key] = value
        print('self.dict di put after ditambah dict[key]', self.dict)
        
        if len(self.dict) > self.capacity:
            for item in self.dict:
                print('self.dict di dihapus ', self.dict[item])
                del self.dict[item]
                break

lRUCache = LRUCache(2)
print()
lRUCache.put(1, 1) # cache is {1=1}
print()
lRUCache.put(2, 2) # cache is {1=1, 2=2}
print()
lRUCache.get(1)    # return 1
print()
lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print()
lRUCache.get(2)    # returns -1 (not found)
print()
lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print()
lRUCache.get(1)    # return -1 (not found)
print()
lRUCache.get(3)    # return 3
print()
lRUCache.get(4)    # return 4
