class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        '''
        abz t = 2
        bcab
        cdba ?
        the string might be empty

        when t = 0 i should only return the original string
        when the string is empty and we have transformation > 0 then we should be returning null
        i will convert string to list and traverse till the t number of transormations
        zzz
        ababab
        i will just return the length of res list
        TC : o(t) * o(m)
        SC : o(m)
        this results in an 
        how many charcters can become Z in the number of operations 
        i can think of having a list of ascii values

        [97, 98, 99, 121, 121] t = 2
        in the following number of operations which char can reach the z
        [99, 101, 102, 123, 123] numbers > 123 i can think of increasing the charcter count len by 1

        [97, 98, 99, 122, 122] t = 26 ((97 - 97) // 26) =
        [1, 1, 1, 2, 2]

        [123, 124,125, 148, 148 ]
        in the following number of operations which char can reach the z
        [99, 101, 102, 123, 123] numbers > 123 i can think of increasing the charcter count len by 1

        TC : O(n)
        SC : O(n)

        So i am thinking like this
        '''
        res = []
        mod = 10 ** 9 + 7
        cnt = [0] * 26
        for i in s:
            cnt[ord(i) - ord('a')] += 1
        
        for i in range(t):
            nxt = [0] * 26
            nxt[0] = cnt[25]
            nxt[1] = (cnt[0] + cnt[25])% mod
            for i in range(2, 26):
                nxt[i] = cnt[i - 1]
            cnt = nxt
        res = sum(cnt) % mod
        return res

            