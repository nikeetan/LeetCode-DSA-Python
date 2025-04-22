class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        word_count = [0] * 26
        unique_chars = set(ransomNote)
        for i in ransomNote:
            word_count[ord(i) - ord('a')] += 1

        for i in magazine:
            word_count[ord(i) - ord('a')] -= 1
        
        for i in unique_chars:
            if word_count[ord(i) - ord('a')] > 0:
                return False
        print(word_count)
        return True
