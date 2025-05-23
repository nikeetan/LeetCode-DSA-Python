class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter_array = [0] * 26
        max_val , max_count = 0, 0
        for task in tasks:
            counter_array[ord('A')-ord(task)] += 1
            if max_val == counter_array[ord('A')-ord(task)]:
                max_count += 1
            elif max_val < counter_array[ord('A')-ord(task)]:
                max_val = counter_array[ord('A')-ord(task)]
                max_count = 1
        

        part_count = max_val - 1
        space = (n - (max_count - 1)) * part_count
        available_tasks = len(tasks) - (max_val * max_count)
        idle = max(0, space - available_tasks)
        return len(tasks) + idle
        # freq_map = {}
        # pq = []
        # time = 0
        # for i in tasks:
        #     if i not in freq_map:
        #         freq_map[i] = 1 
        #     else:
        #         freq_map[i] += 1 
        # occ = freq_map.values()
        # for i in occ:
        #     heapq.heappush(pq,-i)
        # while pq :
        #     cycle = n + 1
        #     store = []
        #     task_count = 0
        #     while (cycle > 0) and (pq):
        #         ele = -heapq.heappop(pq)
        #         if ele > 1:
        #             ele -= 1
        #             store.append(-ele)
        #         task_count += 1
        #         cycle -= 1
        #     for i in store:
        #         heapq.heappush(pq,i)
        #     time += task_count if not pq else n + 1
        # return time
        