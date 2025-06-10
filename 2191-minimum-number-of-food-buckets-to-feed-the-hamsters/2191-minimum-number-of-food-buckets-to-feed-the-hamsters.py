class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        
        food_bucket = 0
        seen = set()
        n = len(hamsters)
        for i in range(n):
            # print(seen)
            # one index that is ['.']
            if i - 1 < 0:
                if hamsters[i] == 'H' and i + 1 >= n:
                    return -1
                elif hamsters[i] == '.'  and i + 1 >= n:
                    return food_bucket
            # last index ['H', '.', '.', 'H', '.', '.', ,'H']
            
            if i + 1 >=n: 
                
                if hamsters[i] == 'H' and hamsters[i - 1] == 'H':
                    return - 1
                elif hamsters[i] == 'H' and (i - 1) not in seen:
                    seen.add(i - 1)
                    food_bucket += 1
                    
                return food_bucket 
                

            # Not possible (if i am at hamsters and adjacent i don't have empty space)
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
            