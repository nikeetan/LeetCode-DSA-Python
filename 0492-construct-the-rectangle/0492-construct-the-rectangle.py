class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        def helper(number:int):
            print(number)
            if area%number==0:
                return [area//number,number]
            return helper(number-1)

        return helper(int(area**0.5))