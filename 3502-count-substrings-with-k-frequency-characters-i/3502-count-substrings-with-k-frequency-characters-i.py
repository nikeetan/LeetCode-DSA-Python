'''
      fp
a a a a
      sp
cnt = 4
map = {a : 1, b : 1, c : 1}

    fp
a b a c b
        sp

a b c d e f
map = {a : 1, b : 1, c : 1, d : 1 , e : 1, f : 1}
break
keys = a, b which is accounting for 2 if i have b 
the movement any one amonst them is lesser than 2 while shrinking i can remove them from the key O(1) because i will be intersted in the first value

TC : O(N + N) ~ O(2N) = O(N * k)
SC : O(N)

'''

class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        '''
        Total number of substrings that can be generated given s
        n = len(s)
        total_sub  = n * (n + 1) // 2
        '''
        n = len(s)
        total_sub = n * (n + 1) // 2
        fp, sp = 0, 0
        counter = defaultdict(int)
        while sp < n:
            counter[s[sp]] += 1 
            while counter[s[sp]] >= k:
                counter[s[fp]] -= 1
                fp += 1
            total_sub = total_sub - (sp - fp + 1)
            sp += 1
        return total_sub


        
        '''
        count = 0
        for i in range(len(s)):
            counter = [0] * 26
            count_flag = 0
            for j in range(i, len(s)):
                counter[ord(s[j]) - ord('a')] += 1
                if counter[ord(s[j]) - ord('a')] >= k:
                    count += len(s) - j 
                    break
        return count
        '''


                

                
'''
abcde
'''

