class Solution:
    def maxDiff(self, num: int) -> int:
        convert_max = list(str(num))
        convert_min = list(str(num))
        first_digit = -1
        for indx, val in enumerate(convert_max):
            if val != '9' and first_digit == -1:
                first_digit = val 
            if val == first_digit:
                convert_max[indx] = '9'
        if len(set(convert_min)) == 1:
            i = 0
            while i < len(convert_min):
                convert_min[i] = '1'
                i += 1
        else:
            min_digit = convert_min[0]
            i = 0
            min_val = -1
            replace = -1
            while i < len(convert_min):
                if convert_min[i] == '1' or  convert_min[i] == '0':
                    i += 1
                    continue
                else:
                    if min_val == -1:
                        min_val = convert_min[i]
                        if i == 0:
                            replace = '1'
                        else:
                            replace = '0'
                    if min_val == convert_min[i]:
                        convert_min[i] = replace
                i += 1

        return int(''.join(convert_max)) - int(''.join(convert_min))


        