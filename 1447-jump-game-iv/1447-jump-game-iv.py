class Solution:
    def minJumps(self, arr: List[int]) -> int:
        dic = defaultdict(list)
        for i in range(len(arr)):
            dic[arr[i]].append(i)
       
       
        
        
        queue = deque([(0, 0)])
        visited = set()
        visited.add(0)
        n = len(arr)
        while queue:
            
            curr_indx, steps = queue.popleft()
            if curr_indx >= n - 1:
                return steps

            next_nei = curr_indx + 1
            prev_nei = curr_indx - 1

            if arr[curr_indx] in dic:
                for jump in dic[arr[curr_indx]]:
                    if ((jump != curr_indx) and (jump not in visited)):
                        queue.append((jump, steps + 1))
                        visited.add(jump)
                del dic[arr[curr_indx]]
            

            if next_nei < n and next_nei not in visited:
                queue.append((next_nei, steps + 1))
                visited.add(next_nei)

            if prev_nei >= 0 and prev_nei not in visited:
                queue.append((prev_nei, steps + 1))
                visited.add(prev_nei)
        
        return -1
