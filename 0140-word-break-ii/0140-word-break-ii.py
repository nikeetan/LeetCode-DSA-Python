class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        part = []
        wordDict = set(wordDict)
        def dfs(indx, part):
            if indx >= len(s):
                ans = ' '.join(part[:])
                res.append(ans)
                return True
            for w in wordDict:
                if s[indx : indx + len(w)] == w:
                    part.append(s[indx : indx + len(w)])
                    dfs(indx + len(w), part)
                    part.pop()
        dfs(0, [])
        return res            
