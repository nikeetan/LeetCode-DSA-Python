'''
join the list of string by a delimiter
and then split the string by the same delimiter
'''

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        self.delimiter = str(len(strs))+"encoded"
        encoded_str = self.delimiter.join(strs)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_str = list(s.split(self.delimiter))
        return decoded_str
    
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))