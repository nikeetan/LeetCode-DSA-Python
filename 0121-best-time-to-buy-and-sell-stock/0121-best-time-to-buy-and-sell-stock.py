class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        lets say we have a pointer where i buy a first stock and it keeps on searching from inner loop 
        statrting from ith + 1 index 
        outer for loop runs till penultimate index
        by this what we are making sure is we are not buying anything on day 2 and selling it on day 1

        profit = 0
        for purchased in range(len(prices) -1 ):
            for sold in range(purchased+1 ,len(prices) ):
                profit = max(profit , prices[sold] - prices[purchased])

        time complexity is O(n2) n is the size of number of prices
        space complecity is o(1)


        [7,1,5,3,6,4]
        # Itr 1
        p1 = 0
        p2 = 1
        profit = 0

        # Itr 2
        p1 = 1
        p2 = 2
        profit = 5
         
        # Itr 3
        p1 = 1
        p2 = 2
        profit = 5


     
        '''
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
        return max_profit
