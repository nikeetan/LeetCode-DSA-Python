class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        '''
        i am thinking like lets say we have a number whose freq is more in tops and 
        and we check the tops with the index where there is different frequency we will try to see the value in bottom if that doesn't match then we can't swap tops then we will go for bottom we will do the process and then if both the times we get -1 

        '''
        def swap_dominoes(ele):
            rotations = 0
            rotation_top, rotation_bottom = 0, 0
            for top, bottom in zip(tops, bottoms):
                if top != ele and bottom != ele:
                    return -1
                elif top!= ele:
                    rotation_top += 1
                elif bottom != ele:
                    rotation_bottom += 1
            return min(rotation_top, rotation_bottom)

        rotations = swap_dominoes(tops[0])
        if rotations != -1 or tops[0] == bottoms[0]:
            return rotations
        else:
            return swap_dominoes(bottoms[0])