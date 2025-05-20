class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return 0
        dic = defaultdict(list)
        for i in range(len(arr)):
            dic[arr[i]].append(i)
        n = len(arr)
        front, back = set([0]), set([n- 1])
        visited = {0, len(arr) - 1}
        n = len(arr)
        steps = 0
        while front:
            if len(front) > len(back):
                front, back = back, front
            next_front = set()
            for curr_indx in front:
                for indx in dic[arr[curr_indx]]:
                    if indx in back:
                        return steps + 1
                    if indx not in visited:
                        next_front.add(indx)
                        visited.add(indx)
            
                dic[arr[curr_indx]].clear()

                next_indx = curr_indx + 1
                prev_indx = curr_indx - 1
                
                if (0 <= next_indx < len(arr)):
                    if next_indx in back:
                        return steps + 1
                    if next_indx not in visited:
                        next_front.add(next_indx)
                        visited.add(next_indx)
                if (0 <= prev_indx < len(arr)):
                    if prev_indx in back:
                        return steps + 1
                    if prev_indx not in visited:
                        next_front.add(prev_indx)
                        visited.add(prev_indx)
            front = next_front
            steps += 1
        return -1



# class Solution:
#     def minJumps(self, arr) -> int:
#         n = len(arr)
#         if n <= 1:
#             return 0

#         graph = {}
#         for i in range(n):
#             if arr[i] in graph:
#                 graph[arr[i]].append(i)
#             else:
#                 graph[arr[i]] = [i]

#         curs = set([0])  # store layers from start
#         visited = {0, n-1}
#         step = 0

#         other = set([n-1]) # store layers from end

#         # when current layer exists
#         while curs:
#             # search from the side with fewer nodes
#             if len(curs) > len(other):
#                 curs, other = other, curs
#             nex = set()

#             # iterate the layer
#             for node in curs:

#                 # check same value
#                 for child in graph[arr[node]]:
#                     if child in other:
#                         return step + 1
#                     if child not in visited:
#                         visited.add(child)
#                         nex.add(child)

#                 # clear the list to prevent redundant search
#                 graph[arr[node]].clear()

#                 # check neighbors
#                 for child in [node-1, node+1]:
#                     if child in other:
#                         return step + 1
#                     if 0 <= child < len(arr) and child not in visited:
#                         visited.add(child)
#                         nex.add(child)

#             curs = nex
#             step += 1

#         return -1