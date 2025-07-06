class Solution {
    public int lastStoneWeight(int[] stones) {
        if (stones.length == 1){
            return stones[0];
        }
        else{
            PriorityQueue <Integer> maxHeap = new PriorityQueue<>();
            int x, y;
            for (int i = 0; i < stones.length; i ++ ){
                maxHeap.add(-1 * stones[i]);
            }
            while(maxHeap.size()>=2){
                y = maxHeap.poll();
                x = maxHeap.poll();
                if(x == y){
                    continue;
                }
                else{
                    y = ((-1 * y) - ( -1 * x));
                    maxHeap.add(-1 * y);
                }
            }
            if(maxHeap.size() == 0){
                return 0;
            }
            else if (maxHeap.size() > 1){
                y = maxHeap.poll();
                x = maxHeap.poll();
                if (y == x){
                    return 0;
                }
                return ((-1 * y) - (-1 * x));
            }
            return -1 * maxHeap.poll();
        }
    }
}