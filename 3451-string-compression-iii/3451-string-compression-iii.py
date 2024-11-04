class Solution:
    def compressedString(self, word: str) -> str:
        if len(word)==0:
            return word
        else:
            to_return=''
            count = 1
            for i in range(1,len(word)):
                if word[i]==word[i-1]:
                    count+=1
                else:
                    if count<9:
                        if to_return:
                            to_return+=str(count)+word[i-1]
                        else:
                            to_return=str(count)+word[i-1]
                    else:
                        while count > 9:
                            if to_return:
                                to_return += '9' + word[i-1]
                            else:
                                to_return = '9' + word[i-1]
                            count -= 9
                        if count>0:
                            to_return +=str(count)+word[i-1]
                    count =1
            if count > 9:
                while count > 9:
                    if to_return:
                        to_return += '9' + word[i-1]
                    else:
                        to_return = '9' + word[i-1]
                    count -= 9
                if count>0:
                    to_return +=str(count)+word[i-1]
            else:
                to_return+=str(count)+word[-1]
            return to_return

                
                