class Solution:
    # def helper(self,s1,p1,length,choice,store):
    #     if p1==length:
    #         store.append("".join(choice))
    #         return
    #     else:
    #         for i in range(p1,length):
    #             s1[p1],s1[i]=s1[i],s1[p1]
    #             self.helper(s1,p1+1,length,choice+s1[p1],store)
    #             s1[p1],s1[i]=s1[i],s1[p1]

    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        can i check the occurance and say
        '''
        l1,l2=len(s1),len(s2)
        if l1>l2:
            return False
        else:
            count=l1
            new_s1=[0]*26
            new_s2=[0]*26
            for i in range(l1):
                new_s1[ord(s1[i]) - ord('a')] += 1
                new_s2[ord(s2[i]) - ord('a')] += 1
            
            for i in range(l1, l2):
                if new_s1 == new_s2:
                    return True
                new_s2[ord(s2[i]) - ord('a')] += 1
                new_s2[ord(s2[i - l1]) - ord('a')] -= 1
            return new_s1==new_s2


        # s1=list(s1)
        # p1=0
        # length=len(s1)
        # choice=""
        # store=[]
        # self.helper(s1,p1,length,choice,store)
        # to_compare=list(s2[0:len(s1)])
        # if "".join(to_compare) in store:
        #     return True
        # else:    
        #     p2=len(s1)
        #     while p2<len(s2):
        #         to_compare.pop(0)
        #         to_compare.append(s2[p2])
        #         if "".join(to_compare) in store:
        #             return True
        #         p2+=1
        # return False
            