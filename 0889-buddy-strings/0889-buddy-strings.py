'''
i should only swap two letters
'''

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        goal_map  = {}
        s_map = {}
        for i in goal:
            if i not in goal_map:
                goal_map[i] = 1
            else:
                goal_map[i] += 1
        for i in s:
            if i not in s_map:
                s_map[i] = 1
            else:
                s_map[i] += 1
        
        curr_indx = 0
        chr_count = 0
        equal_chars = 0
        while curr_indx < len(s):
            if s[curr_indx] not in goal_map:
                return False
            
            if s[curr_indx] in goal_map and s[curr_indx] != goal[curr_indx]:
                chr_count += 1
                if s_map[s[curr_indx]] - 1 == 0:
                    del s_map[s[curr_indx]]
                else:
                    s_map[s[curr_indx]] -= 1
                if goal_map[s[curr_indx]] - 1 == 0:
                    del goal_map[s[curr_indx]]
                else:
                    goal_map[s[curr_indx]] -= 1

            elif s[curr_indx] == goal[curr_indx] and s_map[s[curr_indx]] > 1 and s_map[s[curr_indx]] == goal_map[s[curr_indx]]:
                equal_chars = 2
                if s_map[s[curr_indx]] - 1 == 0:
                    del s_map[s[curr_indx]]
                    del goal_map[s[curr_indx]]
                else:
                    s_map[s[curr_indx]] -= 1
                    goal_map[s[curr_indx]] -= 1
            curr_indx += 1
        #print(chr_count, equal_chars)
        if chr_count > 2:
            return False
        elif chr_count == 2 or equal_chars == 2:
            return True
        return False