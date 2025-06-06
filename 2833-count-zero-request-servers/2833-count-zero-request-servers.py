'''
5, 6 =  [5, 10]
'''

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        logs.sort(key = lambda x : x[1])
        res = [0] * len(queries)
        cnt = Counter()
        used_cnt = 0
        i, j = 0, 0
        for [t, id] in sorted([t, id] for id ,t in enumerate(queries)):
            while i < len(logs) and logs[i][1] <= t:
                cnt[logs[i][0]] += 1
                if cnt[logs[i][0]] == 1:
                    used_cnt += 1
                i += 1
            while j < i and logs[j][1] < t - x:
                cnt[logs[j][0]] -= 1
                if cnt[logs[j][0]] == 0:
                    used_cnt -= 1
                j += 1
            res[id] = n - used_cnt
        return res
            



            

