'''
generate all subsequence and traverse each subsequence to find the difference whether they are 1 if yes then record the length in  a variable maximum and always it will be a max(curr_maximum , new_subseqlen)
'''

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        numMap = {}
        for i in nums:
            if i not in numMap:
                numMap[i] = 1
            else:
                numMap[i] += 1

        # two pointers
        subseq_count = 0
        for key, val in numMap.items():
            if key + 1 in numMap:
                subseq_count = max(subseq_count, numMap[key] + numMap[key + 1])
        return subseq_count
        

'''
test case
[1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2]
numMap = {1 : 1 , 2 : 3, 3 : 2, 5 : 1, 7 : 1}
[1, 2,  2,  2,  3,  3,  5,  7]
                        fp  sp
subseqLen = 5


[-3,-1,-1,-1,-3,-2]

[-3, -3, -2, -1, -1, -1]
     fp.  sp

'''