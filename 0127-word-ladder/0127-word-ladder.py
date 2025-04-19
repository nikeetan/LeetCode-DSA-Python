class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        everytime there is a char changed by position i will add it in a queue if its not visited we can perform BFS
        '''
        queue = deque([(beginWord, 1)])
        chars = "abcdefghijklmnopqrstuvwxyz"
        visited = set()
        wordList = set(wordList)
        while queue:
            word, level = queue.popleft()
            visited.add(word)
            # now word transformation lets say i have hit
            # i will covert into list of character so ['h' ,'i' ,'t']
            # ['a','i','t']['b','i','t'],['c','i','t']
            if word == endWord:
                return level 
            pos = 0
            while pos < len(word):
                temp = list(word)
                for i in chars:
                    temp[pos] = i
                    new_word = ''.join(temp)
                    if (new_word not in visited) and (new_word in wordList):
                        queue.append((new_word, level+1))
                pos += 1
        return 0
                