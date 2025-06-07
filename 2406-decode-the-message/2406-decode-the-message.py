class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        start = ord('a')
        res = ""
        decode_map = collections.defaultdict(int)
        for i in key:
            if i == ' ':
                continue
            if i not in decode_map:
                decode_map[i] = chr(start)
                start += 1
        for i in message:
            if i == ' ':
                res += i
            else:
                res += decode_map[i]
        return res
