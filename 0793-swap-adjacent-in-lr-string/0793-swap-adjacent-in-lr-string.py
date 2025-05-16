'''
edge case here would be lets say if i have string length of only one then i will compare are both equal and if yes will return True else False 
I am thinking of converting into list both the strings and after that assigining two pointers for the first list and next two pointers for the next list and then checking the first two indices of the start == next two indices of the result if yes then move fp by 2 and sp by 2 in both of them 
'''

class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        p1, p2 = 0, 0
        n = len(start)
        while p1 < n or p2 < n:
            while p1 < n and start[p1] == 'X':
                p1 += 1 
            while p2 < n and result[p2] == 'X':
                p2 += 1
            
            if (p1 == n) != (p2 == n):
                return False
            if (p1 == n) and (p2 == n):
                return True
            if start[p1] != result[p2]:
                return False
            
            if p1 > p2 and start[p1] == 'R':
                return False
            elif p1 < p2 and start[p1] == 'L':
                return False
    
            p1 += 1
            p2 += 1

        return True
        
        