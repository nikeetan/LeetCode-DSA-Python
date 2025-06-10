class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        hamsters = list(hamsters)
        n = len(hamsters)
        for i in range(n):
            if hamsters[i] == 'H':
                if i > 0 and hamsters[i - 1] == 'B':
                    continue
                elif i < n - 1 and hamsters[i + 1] == '.':
                    hamsters[i + 1] = 'B'
                elif i > 0 and hamsters[i - 1] == '.':
                    hamsters[i - 1] = 'B'
                else:
                    return -1
        food_count = 0
        for i in hamsters:
            if i == 'B':
                food_count += 1
        return food_count
        '''
        food_bucket = 0
        seen = set()
        n = len(hamsters)
        for i in range(n):
            if i - 1 < 0:
                if hamsters[i] == 'H' and i + 1 >= n:
                    return -1
                elif hamsters[i] == '.'  and i + 1 >= n:
                    return food_bucket            
            if i + 1 >=n: 
                if hamsters[i] == 'H' and hamsters[i - 1] == 'H':
                    return - 1
                elif hamsters[i] == 'H' and (i - 1) not in seen:
                    seen.add(i - 1)
                    food_bucket += 1
                return food_bucket 
    
            if hamsters[i] == 'H':
                if (i - 1 > 0) and (hamsters[i - 1] != '.'  and hamsters[i + 1] != '.'):
                        return -1
                elif (i - 1 < 0) and hamsters[i + 1] != '.':
                        return -1
                else:               
                    if hamsters[i + 1] == '.':
                        if i - 1 not in seen:
                            seen.add(i + 1)
                            food_bucket += 1
                    elif hamsters[i - 1] == '.':
                        if i - 1 not in seen:
                            seen.add(i - 1)
                            food_bucket += 1
        return food_bucket
        '''
            