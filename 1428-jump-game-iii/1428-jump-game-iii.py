class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])
        visited = set()
        visited.add(start)
        n = len(arr)
        while queue:
            curr_indx = queue.popleft()
            if arr[curr_indx] == 0:
                return True
            next_nei = curr_indx + arr[curr_indx]
            prev_nei = curr_indx - arr[curr_indx]
            if next_nei < n and next_nei not in visited:
                queue.append(next_nei)
                visited.add(next_nei)
            if prev_nei >= 0 and prev_nei not in visited:
                queue.append(prev_nei)
                visited.add(prev_nei)
        return False

            
