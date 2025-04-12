'''
min_heap
{
    foo : [(1,foo)]
}
'''


class TimeMap:

    def __init__(self):
        self.set_word = {}
     
    def set(self, key: str, value: str, timestamp: int) -> None:
        # We are setting the first key value pair for the hashmap
        if key not in self.set_word:
            self.set_word[key] = []
        self.set_word[key].append((timestamp,value))
    def get(self, key: str, timestamp: int) -> str:
    
        if key not in self.set_word:
            return ""

        timeprev = self.set_word[key]
        #timeprev = [key for key, value in word_dict.items()]
        
        low , high = 0, len(timeprev) - 1
        def search(timeprev, timestamp, low, high):
            ans = ""
            while low <= high:
                mid = low + (high - low)//2
                if timeprev[mid][0] <= timestamp:
                    ans = timeprev[mid][1]
                    low = mid + 1
                else:
                    high = mid - 1
            return ans
        ans = search(timeprev, timestamp, low, high)
        return ans