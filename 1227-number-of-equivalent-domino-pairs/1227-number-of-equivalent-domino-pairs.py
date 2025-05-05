class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        '''
        Two pointers 
        brute force is two for loop traversing the list until i am at the last but one
        '''
        # p1 = 0
        # count = 0
        # while p1 < len(dominoes) - 1:
        #     a, b = dominoes[p1]
        #     p2 = p1 + 1
        #     while p2 < len(dominoes):
        #         c, d = dominoes[p2]
        #         if ((a == c) and (b == d)) or ((a == d) and (b == c)):
        #             count += 1
        #         p2 += 1 
        #     p1 += 1
        # return count
        hash_map = {}
        count = 0
        for domino in dominoes:
            a, b = domino
            key = tuple(sorted((a , b)))
            if len(hash_map) == 0:
                hash_map[key] = 1
            else:
                if key in hash_map:
                    count += hash_map[key]
                    hash_map[key] += 1
                else:
                    hash_map[key] = 1
        return count 

