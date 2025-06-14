'''
brute force 
hash_map = {}
traverse whole matrix and then have a key value if any value of a key is less than n then i will return false
'''
import collections
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        #hash_map = collections.defaultdict(int)
        n = len(matrix)
        i = 0
        while i < n:
            hash_map = collections.defaultdict(int)
            for row in range(n):
                hash_map[matrix[row][i]] += 1
            for key, val in hash_map.items():
                if val != 1:
                    return False
            hash_map = collections.defaultdict(int)
            for col in range(n):
                hash_map[matrix[i][col]] += 1
            for key, val in hash_map.items():
                if val != 1:
                    return False
            #print(hash_map)
           
            i += 1
        return True