class Solution {
    public int numberOfChild(int n, int k) {
        int cycle, mod;
        cycle = k / (n - 1);
        mod = k % (n - 1);
        if (cycle % 2 == 0)
        {
            return mod;
        }
        else
        {
            return n - 1 - mod;
        }


    }
}