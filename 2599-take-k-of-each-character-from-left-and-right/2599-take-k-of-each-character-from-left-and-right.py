class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        count_arr=[0,0,0]
        for i in range(len(s)):
            count_arr[ord(s[i])-ord('a')]+=1

        if min(count_arr)<k:
            return -1
        else:
            left,right=0,0
            win_size=float('inf')
            while right<len(s):
                count_arr[ord(s[right])-ord('a')]-=1
                while min(count_arr)<k:
                    count_arr[ord(s[left])-ord('a')]+=1
                    left+=1
                win_size=min(win_size,len(s)-(right-left+1))
                right+=1
            return win_size




        