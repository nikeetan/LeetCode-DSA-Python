class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr=sorted(arr)
        check=abs(arr[0]-arr[1])
        for i in range(1,len(arr)-1):
            if abs(arr[i]-arr[i+1])!=check:
                return False
        return True
        