class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_map = {}
        magazine_map = {}
        for i in ransomNote:
            if i not in ransom_map:
                ransom_map[i] = 1
            else:
                ransom_map[i] += 1
        for i in magazine:
            if i not in magazine_map:
                magazine_map[i] = 1
            else:
                magazine_map[i] += 1
        compare_keys = list(ransom_map.keys())
        for i in compare_keys:
            if i not in magazine_map:
                return False
            elif ransom_map[i] > magazine_map[i]:
                return False
        return True
            


        