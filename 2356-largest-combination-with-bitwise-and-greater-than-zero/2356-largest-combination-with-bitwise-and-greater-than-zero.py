class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        freq=0
        max_freq=0
        for i in range(32):
            freq=0
            for ele in candidates:
                if (ele & (1<<i)):
                    freq+=1
            max_freq=max(freq,max_freq)
        return max_freq


        