class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        '''
        max _heap of occurance
        '''
        fruit_type = collections.defaultdict(int)
        left, right = 0, 0
        while right < len(fruits):
            fruit_type[fruits[right]] += 1
            if len(fruit_type) > 2:
                if fruit_type[fruits[left]] - 1 == 0:
                    del  fruit_type[fruits[left]]
                else:
                    fruit_type[fruits[left]] -= 1
                left += 1
            right += 1
        return right - left
