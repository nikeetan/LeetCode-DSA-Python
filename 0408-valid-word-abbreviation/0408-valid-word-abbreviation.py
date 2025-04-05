class Solution:

    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        p1 , p2 = 0 , 0
        while ((p1 < len(abbr)) and (p2 < len(word))):
            if abbr[p1] >= 'a' and abbr[p1] <= 'z' :
                if abbr [p1] == word [p2]:
                    p1 += 1
                    p2 += 1
                    continue
                else:
                    return False
            else:
                if abbr[p1] == '0':
                    return False
                else:
                    cnt = ''
                    while (abbr[p1] < 'a') and (p1<len(abbr)):
                        print(abbr[p1])
                        cnt += abbr[p1]
                        p1 += 1
                        if p1 >= len(abbr):
                            break
                    cnt = int(cnt)
                    p2 += cnt
        if p1 == len(abbr) and p2 == len(word) :
            return True
        else:
            return False