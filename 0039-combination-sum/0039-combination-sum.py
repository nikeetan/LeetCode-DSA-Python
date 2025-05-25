class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        pick and non pick
        sort the array
        [2, 3, 6, 7]
        itr 1: choose
        p1
        [2, 3, 6, 7]
        sum = 2
        sum = 4
        sum = 6
        sum = 8 
        8 > 7
        return
        from 6 i will now move pointer that is to 3 since i have sorted array if i move pointer i will always get the sum greater than 7 but i can't get it untill i do 
        '''
        '''
        candidates.sort()
        size = len(candidates)
        candidates_set = []
        res = []
        def helper(indx, target, candidates_set):
            if indx >= size or target < 0:
                return
            elif indx < size and target == 0:
                res.append(candidates_set[:])
                return
            # pick
            for i in range(indx, size):
                candidates_set.append(candidates[i])
                helper(i, target - candidates[i], candidates_set)
                candidates_set.pop()

            # # Non pick
            # helper(indx + 1, target, candidates_set)
        helper(0, target, candidates_set)
        return res
        '''
        dp = [[] for i in range(target + 1)]
        dp[0].append([])   
        # Outer for loop is it possible to make sum 1 form the current set of numbers
        # inner loop is think like coin change which all possible coins could make
        for i in range(1, target + 1):
            for j in range(len(candidates)):
                if candidates[j] <= i:
                    for comb in dp[i - candidates[j]]:
                        comb = comb + [candidates[j]]
                        comb.sort()
                        if comb not in dp[i]:
                            dp[i].append(comb)        
        return dp[target]


