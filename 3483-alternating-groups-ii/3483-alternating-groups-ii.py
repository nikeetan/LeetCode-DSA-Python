class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:

        ### Two passes
        
        a_c=1
        p1,p2=0,1
        t_c=0
        while p2<len(colors):
            if colors[p1]==colors[p2]:
                a_c=1
                p1=p2
                p2=p1+1
                continue
            a_c+=1
            if a_c>=k:
                t_c+=1
            p1+=1
            p2+=1
        last_ele=colors[-1]
        for i in range(k-1):
            if last_ele==colors[i]:
                break
            a_c+=1
            if a_c>=k:
                t_c+=1
            last_ele=colors[i]
        return t_c
       
        '''
        colors=colors+colors[0:k-1]
        count=0
        p1,p2=0,1
        while p2<len(colors): 
            if colors[p2]==colors[p2-1]:
                p1=p2
            if p2-p1+1==k:
                count+=1
                p1=p1+1
            p2+=1
        return count
        '''
