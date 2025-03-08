class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_b=0
        p1,p2=0,0
        mini_rep=float('inf')
        while p2<k:
            if blocks[p2]=='W':
                white_b+=1
            p2+=1
        mini_rep=min(mini_rep,white_b)
        while p2<len(blocks):
            if blocks[p1]=='W':
                white_b-=1
            if blocks[p2]=='W':
                white_b+=1
            mini_rep=min(mini_rep,white_b)
            p1+=1
            p2+=1
        return mini_rep
        
            