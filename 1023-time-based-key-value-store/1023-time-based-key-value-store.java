class Pair{
    String x;
    int y;
    Pair(String x, int y)
    {
        this.x = x;
        this.y = y;
    }
}

class TimeMap {

    private HashMap <String, List<Pair>> map;
    public TimeMap() {
        this.map = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        List<Pair> temp;
        if (!map.containsKey(key)){
            temp = new ArrayList<>();
            map.put(key, temp);
        }
        else{
            temp = map.get(key);
        }
          temp.add(new Pair(value, timestamp));
    }
    
    public String get(String key, int timestamp) {
        if(!map.containsKey(key)){
            return "";
        }
        else{
            List<Pair> data;
            data = map.get(key);
            int left = 0, right = data.size() - 1, mid;
            int ans = -1;
            while (left <= right){
                mid = left + (right - left) / 2;
                if (data.get(mid).y <= timestamp){
                    ans = mid;
                    left = mid + 1;
                } 
                else{
                    right = mid - 1; 
                }
            }
            if(ans == -1){
                return "";
            }
            else{
                return data.get(ans).x;
            }
        }
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */