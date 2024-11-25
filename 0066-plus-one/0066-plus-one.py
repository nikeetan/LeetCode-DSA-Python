class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        k=int("".join(map(str,digits)))
        k=k+1
        k=str(k)
        new_list=[int(x) for x in k]
        return new_list
    