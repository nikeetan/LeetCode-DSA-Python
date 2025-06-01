'''
topological sort
'''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordDict = set(wordDict)
        queue = deque([0])
        seen = set()
        while queue:
            print(queue)
            start = queue.popleft()
            if start == len(s):
                return True
            for i in range(start, len(s)):
                if i in seen:
                    continue
                if s[start : i + 1] in wordDict:
                    queue.append(i + 1)
                    seen.add(i)
        return False
