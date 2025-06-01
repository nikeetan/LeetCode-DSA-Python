class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = defaultdict(list)
        for i in range(len(s) - 1, -1 , -1):
            valid_sentence = []
            for w in wordDict:
                if i + len(w) <= len(s) and s[i : i + len(w)] == w:
                    if i + len(w) == len(s):
                        valid_sentence.append(w)
                    else:
                        sentences = dp[i + len(w)]
                        for sentence in sentences:
                            valid_sentence.append(w + " " + sentence)

            dp[i] = valid_sentence
        return dp[0]
        

        '''
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
        '''
