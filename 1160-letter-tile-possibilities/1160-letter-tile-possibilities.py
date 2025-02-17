class Solution:
    
    def helper(self,tiles,bl,sl,index):
        if sl:
            bl.add(''.join(sl))
        for i in range(index,len(tiles)):
            tiles[i],tiles[index]=tiles[index],tiles[i]
            self.helper(tiles,bl,sl+[tiles[index]],index+1)
            tiles[i],tiles[index]=tiles[index],tiles[i]
        

    '''     
    def helper(self,char_count): 
        total_cnt=0
        for i in range(26):
            if char_count[i]==0:
                continue
            total_cnt+=1
            char_count[i]-=1
            total_cnt+=self.helper(char_count)
            char_count[i]+=1
        return total_cnt  
    '''


    def numTilePossibilities(self, tiles: str) -> int:
        tiles=list(tiles)
        bl=set()
        sl=[]
        index=0
        self.helper(tiles,bl,sl,index)
        print(bl)
        return len(bl)



        '''
        char_count=[0]*26
        total_cnt=0
        for i in tiles:
            char_count[(ord(i)-ord('A'))]+=1
        return self.helper(char_count)
        '''


        
        