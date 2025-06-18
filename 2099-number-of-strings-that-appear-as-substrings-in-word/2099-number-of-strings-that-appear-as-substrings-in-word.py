class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        cnt_sub_str = 0
        for sub_str in patterns:
            if sub_str in word:
                cnt_sub_str += 1
        return cnt_sub_str