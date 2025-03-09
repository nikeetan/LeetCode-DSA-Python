class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        last_c=colors[0]
        a_c=1
        t_c=0
        ln=len(colors)
        for i in range(1,ln+k-1):
            if last_c==colors[i%ln]:
                a_c=1
                last_c=colors[i%ln]
                continue
            a_c+=1
            if a_c>=k:
                t_c+=1
            last_c=colors[i%ln]
        return t_c
