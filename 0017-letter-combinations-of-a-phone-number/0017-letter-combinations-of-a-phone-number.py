class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        d_to_w = {2 : "abc", 3 : "def", 4 :"ghi", 5 : "jkl", 6 : "mno", 7 : "pqrs", 8 : "tuv" , 9 : "wxyz"}
        res = []
        def helper(indx, sl):
            if len(sl) == len(digits):
                res.append(''.join(sl[:]))
                return
            letters = d_to_w[int(digits[indx])]
            for i in letters:
                sl.append(i)
                helper(indx + 1, sl)
                sl.pop()
        helper(0, [])
        return res



