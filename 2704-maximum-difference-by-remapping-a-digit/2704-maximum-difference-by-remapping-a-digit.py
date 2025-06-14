#99199 - 100 = 99009
#122 = 922 - 

# 9022 ~ 9922 - 0022 = 9900

# whatever it is if i replace the digit MSD by 9 if it is 9 else i will go with the second and make all occurances of it to be 9


from collections import defaultdict
class Solution:
    def minMaxDifference(self, num: int) -> int:
        max_remap = list(str(num))
        min_remap = list(str(num))
        # max_remap
        remap_val = '-1'
        for indx, val in enumerate(max_remap):
            if remap_val == val:
                max_remap[indx] = '9'
            if (val != '9') and (remap_val == '-1'):
                remap_val = val
                max_remap[indx] = '9'
        max_val = int(''.join(max_remap))

        remap_val = min_remap[0]
        for indx, val in enumerate(min_remap):
            if remap_val == val:
                min_remap[indx] = '0'
        min_val = int(''.join(min_remap))
        return max_val - min_val