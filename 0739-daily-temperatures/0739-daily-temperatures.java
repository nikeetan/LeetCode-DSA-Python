class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int [] warmerDays = new int[temperatures.length];
        Stack<Integer> warmerTemp = new Stack<>();
        for(int i = temperatures.length - 1; i >= 0 ; i -= 1)
        {
            if(warmerTemp.size() == 0)
            {
                warmerTemp.push(i);
                warmerDays[i] = 0;
            }
            else
            {
                while ((!warmerTemp.isEmpty()) && (temperatures[warmerTemp.peek()] <= temperatures[i]))
                {
                    warmerTemp.pop();

                }
                if (warmerTemp.isEmpty())
                {
                    warmerDays[i] = 0;
                }
                else
                {
                    warmerDays[i] = warmerTemp.peek() - i;
                }
                warmerTemp.push(i);
            }

        }
        return warmerDays;
    }
}