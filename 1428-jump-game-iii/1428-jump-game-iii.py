class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque([start])
        n = len(arr)
        while queue:
            curr_indx = queue.popleft()
            if arr[curr_indx] == 0:
                return True
            if arr[curr_indx] < 0:
                continue
            jump = arr[curr_indx]
            arr[curr_indx] = -arr[curr_indx]
            next_nei = curr_indx + jump
            prev_nei = curr_indx - jump
            if next_nei < n:
                queue.append(next_nei)
            if prev_nei >= 0:
                queue.append(prev_nei)
              
        return False

            
