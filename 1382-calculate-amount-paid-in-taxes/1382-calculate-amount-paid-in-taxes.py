class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        previous_slab = 0
        earned_amt = 0
        for upper,tax in brackets:
            previous_slab = upper - previous_slab 
            if previous_slab > income:
                previous_slab = income
            income = income - previous_slab
            earned_amt += (previous_slab * tax) / 100
            previous_slab = upper
            if income == 0:
                return earned_amt
        return earned_amt
