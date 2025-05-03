class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        '''
        i am thinking like lets say we have a number whose freq is more in tops and 
        and we check the tops with the index where there is different frequency we will try to see the value in bottom if that doesn't match then we can't swap tops then we will go for bottom we will do the process and then if both the times we get -1 

        '''
        def swap_count(element, top_flag):
            swaps_count = 0
            for top, bottom in zip(tops, bottoms):
                if top != element and bottom != element:
                    return -1
                elif (top_flag and top != element) or (not top_flag and bottom != element):
                    swaps_count += 1
            return swaps_count

        candidates = {tops[0], bottoms[0]}  # 
        min_swaps = float('inf')

        for ele in candidates:
            top_swap = swap_count(ele, True)
            bottom_swap = swap_count(ele, False)
            if top_swap != -1:
                min_swaps = min(min_swaps, top_swap)
            if bottom_swap != -1:
                min_swaps = min(min_swaps, bottom_swap)

        return -1 if min_swaps == float('inf') else min_swaps