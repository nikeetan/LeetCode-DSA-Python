class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        '''
        simple i will have the list of 0th index ele from the list 
        and next time i traverse i do check only 1st index if i found the same ele in the list of 0th index then i wil remove it from the list and if after doing that i am left with only one ele return the same more than 1 then return -1
        '''
        in_degree=[0]*n
        for i in edges:
            in_degree[i[1]]+=1
        to_return=-1

        for i in range(len(in_degree)):
            if in_degree[i]==0 and to_return==-1:
                to_return=i
            elif in_degree[i]==0 and to_return>-1:
                to_return=-1
                return to_return
            else:
                continue
        return to_return


        return 0