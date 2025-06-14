class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def helper(number):
            nonlocal res
            if number > n:
                return 
            res.append(number)
            for i in range(0, 10):
                helper(number * 10 + i)
        for i in range(1, 10):
            helper(i)
        return res