from collections import OrderedDict
class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.k_to_f = {} # (key, (freq, value)}
        self.f_to_k = defaultdict(OrderedDict) # (freq : [{key : val}, {key : val}])
        self.min_freq = 0
       
    def get(self, key: int) -> int:
        # if the key doesn't exist
        if key not in self.k_to_f:
            return -1
        else:
            freq, val = self.k_to_f[key]
            del self.f_to_k[freq][key]
            if len(self.f_to_k[freq]) == 0:
                if self.min_freq == freq:
                    self.min_freq += 1
                del self.f_to_k[freq] 
            freq += 1
            self.f_to_k[freq][key] = val
            self.k_to_f[key] = (freq, val)
            return val

            
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        # update check
        if key in self.k_to_f:
            freq , val = self.k_to_f[key]
            del self.f_to_k[freq][key]
            if len(self.f_to_k[freq]) == 0:
                if self.min_freq == freq:
                    self.min_freq += 1
                del self.f_to_k[freq]
            freq += 1
            self.k_to_f[key] = (freq, value)
            self.f_to_k[freq][key] = value
        else:
            # remove the excess
            freq = 1
            if len(self.k_to_f) >= self.capacity:
                evict_key , evict_value = self.f_to_k[self.min_freq].popitem(last = False)
                if len(self.f_to_k[self.min_freq]) == 0:
                    del self.f_to_k[self.min_freq]
                    self.min_freq += 1
                del self.k_to_f[evict_key]

            self.min_freq = 1
            self.k_to_f[key] = (freq, value)
            self.f_to_k[freq][key] = value
                


            


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)