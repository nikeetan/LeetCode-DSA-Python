/*
Next greater element

*/ 

class Solution {
    public int maxProfit(int[] prices) {
        Stack <Integer> nextGreater = new Stack<>();
        int maxProfit = Integer.MIN_VALUE;
        for(int i = prices.length - 1; i >= 0; i --){
            if (!nextGreater.isEmpty()){
                while(!nextGreater.isEmpty() && nextGreater.peek() < prices[i]){
                    nextGreater.pop();
                }
                if(!nextGreater.isEmpty()){
                    maxProfit = Math.max(maxProfit, nextGreater.peek() - prices[i]);   
                }
                else{
                nextGreater.push(prices[i]);
                }
                
            }
            else{
                nextGreater.push(prices[i]);
                maxProfit = Math.max(maxProfit, 0);   
            }
        }
        return maxProfit;
    }
}