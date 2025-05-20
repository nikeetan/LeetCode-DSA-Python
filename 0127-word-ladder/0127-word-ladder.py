class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        everytime there is a char changed by position i will add it in a queue if its not visited we can perform BFS
        '''
        if endWord not in wordList:
            return 0
        else:
            front = {beginWord}
            back = {endWord}
            chars = "abcdefghijklmnopqrstuvwxyz"
            visited = set()
            wordList = set(wordList)
            steps = 1
            while front and back:
                if len(front) > len(back):
                    front, back = back, front
                next_front = set()
                for word in front:
                # now word transformation lets say i have hit
                # i will covert into list of character so ['h' ,'i' ,'t']
                # ['a','i','t']['b','i','t'],['c','i','t']
                    pos = 0
                    while pos < len(word):
                        temp = list(word)
                        for i in chars:
                            temp[pos] = i
                            new_word = ''.join(temp)
                            if new_word in back:
                                return steps + 1
                            if (new_word not in visited) and (new_word in wordList):
                                next_front.add(new_word)
                                visited.add(new_word)
                        pos += 1
                front = next_front
                steps += 1
            return 0
                    