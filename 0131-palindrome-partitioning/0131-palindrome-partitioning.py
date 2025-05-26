class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def palindrome_chk(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def helper(indx):
            if indx >= len(s):
                res.append(part[:])
                return 
            for i in range(indx, len(s)):
                if palindrome_chk(s, indx, i):
                    part.append(s[indx : i + 1])
                    helper(i + 1)
                    part.pop()
        res = []
        part = []
        helper(0)
        return res