class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        k_string = ""
        left, right = 0, 0
        while right < len(s):
            k_string += s[right]
            if (right - left + 1) == k:
                result.append(k_string)
                left = right + 1
                k_string = ""
            right += 1
        if (right - left) != 0:

            k_string = k_string + fill * (k - (right - left))
            result.append(k_string)
        return result




