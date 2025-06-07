'''
curr_pos = 2 * prev_pos
[ 4, -2, 2, -4]
arr[2 * i + 1] == 2 * arr[2 * i]
# itr 1
1 == 0

{4 : 0, -2 : 1, 2 : 2, -4 : 3}
twice the current _element == next element
pair_set = ((1, 3), (2, 0))
if len(pair_set) == len(pair) //2:
    return True

O(n) + o(n)
SC : o(n) + o(n // 2)

'''

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        indx = 0
        cnt = 0
        num_map = collections.defaultdict(int)
        zero_cnt = 0
        for num in arr:
            if num == 0:
                zero_cnt += 1
            num_map[num] += 1
        if zero_cnt % 2 != 0:
            return False
        arr.sort()
        while indx < len(arr):
            if ((arr[indx] in num_map) and (2 * arr[indx] in num_map)):
                num_map[2 * arr[indx]] -= 1
                if num_map[2 * arr[indx]] == 0:
                    del num_map[2 * arr[indx]]
                num_map[arr[indx]] -= 1
                if num_map[arr[indx]] == 0:
                    del num_map[arr[indx]]
                cnt += 1
            indx += 1
        print(cnt)
        if cnt == len(arr) // 2:
            return True 
        return False

