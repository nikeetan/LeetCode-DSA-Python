from sortedcontainers import SortedList
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        '''
        if i can assign k tasks then can i assign k + 1 
        else can i assign k - 1
        take smaller tasks and workers of larger capacity if the larger capacity workers can handle the smaller tasks then we will then we can increase the size to say  
        '''
        workers.sort()
        tasks.sort()

        def can_assign(k):
            # check the top max k tasks is being satisfied by max k workers cap
            pills_left = pills 
            k_workers = SortedList(workers[len(workers) - k : ])
            for i in range(k - 1, -1 , -1):
                if tasks[i] <= k_workers[-1]:
                    k_workers.pop()
                else:
                    if pills_left == 0:
                        return False
                    l, r = 0 , len(k_workers) - 1
                    indx = len(k_workers)
                    while l <= r:
                        mid = l + (r - l)//2
                        if k_workers[mid] >= tasks[i] - strength:
                            indx = mid
                            r = mid - 1 
                        else:
                            l = mid + 1
                    if indx == len(k_workers):
                        return False
                    pills_left -= 1
                    k_workers.pop(indx)
            return True
                
        l = 0
        r = min(len(workers), len(tasks))
        res = -1
        while l <= r:
            mid = l + (r - l)//2
            if can_assign(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res