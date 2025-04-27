class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        
        indx = 0
        n = len(instructions)
        visited = [False] * n
        score = 0
        while ((indx >=0 and indx < n)):
            # visited check
            if visited[indx]:
                break
            visited[indx] = True
            if instructions[indx] == "jump":
                new_indx = values[indx] + indx
                # self loop
                if new_indx == indx:
                    break
                indx = new_indx
            elif instructions[indx] == "add":
                score += values[indx]
                indx += 1
        return score
            
            



