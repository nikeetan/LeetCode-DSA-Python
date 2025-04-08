class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))  
            print(key)
            anagram_map[key].append(word)
        return list(anagram_map.values())