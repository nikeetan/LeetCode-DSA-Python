class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:len(s1)])

        if s1_counter == s2_counter:
            return True
        l = 0 
        for r in range(len(s1), len(s2)):
            s2_counter[s2[r]] += 1
            if s2_counter[s2[l]] - 1 == 0:
                del s2_counter[s2[l]]
            else:
                s2_counter[s2[l]] -= 1
            l += 1
            if s2_counter ==  s1_counter:
                return True
        return False
