class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.order = []
    
    @property
    def cache(self):
        if self.order:
            oldest_key = self.order[0]
            return (oldest_key, self.cache[oldest_key])
        return None
    
    @cache.setter
    def cache(self, new_elem):
        key, value = new_elem
        
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            self.cache[key] = value
            return
        
        if len(self.cache) >= self.capacity:
            oldest = self.order.pop(0)
            del self.cache[oldest]
        
        self.cache[key] = value
        self.order.append(key)
    
    def get(self, key):
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return None
    
    def print_cache(self):
        print("LRU Cache:")
        for key in self.order:
            print(f"{key} : {self.cache[key]}")

cache = LRUCache(3)
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")
cache.print_cache()
print(cache.get("key2"))
cache.cache = ("key4", "value4")
cache.print_cache()
