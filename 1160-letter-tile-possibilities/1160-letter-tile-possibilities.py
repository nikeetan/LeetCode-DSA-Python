class Solution:
    def helper(self,tiles,bl,sl,index):
        if index==len(tiles):
            if sl:
                bl.add(''.join(sl))
            return
        for i in range(index,len(tiles)):
            tiles[i],tiles[index]=tiles[index],tiles[i]
            self.helper(tiles,bl,sl+[tiles[index]],index+1)
            self.helper(tiles,bl,sl,index+1)
            tiles[i],tiles[index]=tiles[index],tiles[i]
            

    def numTilePossibilities(self, tiles: str) -> int:
        tiles=list(tiles)
        bl=set()
        sl=[]
        index=0
        self.helper(tiles,bl,sl,index)
        return len(bl)

        