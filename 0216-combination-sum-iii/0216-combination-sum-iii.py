class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:        
        numbers = []
        res = []
        start = 1
        def backtrack(numbers , target, start):
            # base conditions

            if len(numbers) >= k and target == 0:
                res.append(numbers[:])
                return 
            elif len(numbers) >= k and target != 0:
                return
        
            for i in range(start, 10):

                numbers.append(i)
                backtrack(numbers, target - i, i + 1)
                numbers.pop() # handles the backtracking part

        backtrack(numbers , n, start)
        return res
                