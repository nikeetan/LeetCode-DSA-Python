'''
min_heap
{
    foo : [(1,foo)]
}
'''


class TimeMap:

    def __init__(self):
        self.store = {} # hash_map to store the TimeMap
     
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(value, timestamp)]
        else:
            self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:

            timestamps = self.store[key] # here the list will be fetched
            
            l, r = 0, len(self.store[key]) - 1
            ans = -1
            print(timestamps)
            while l <= r:
                mid = l + (r - l)//2
                if timestamps[mid][-1] <= timestamp:
                    ans = mid
                    l = mid + 1
                else:
                    r = mid - 1
            if ans == -1:
                return ""
            else:
                return timestamps[ans][0]
        else:
            return ""