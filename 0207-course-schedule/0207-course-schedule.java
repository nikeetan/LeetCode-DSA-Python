class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int [] indegree = new int[numCourses];
        HashMap<Integer, List<Integer>> preMap = new HashMap<>();
        HashSet<Integer> seen = new HashSet<>();
        for(int i = 0; i < numCourses; i++){
            preMap.put(i, new ArrayList<>());
        }
        for(int [] edges : prerequisites){
            int u = edges[0];
            int v = edges[1];
            indegree[u] += 1;
            preMap.get(v).add(u);
        }
        Queue<Integer> queue = new LinkedList<>();
        for(int i = 0; i < numCourses; i++){
            if (indegree[i] == 0){
                queue.add(i);
            }
        }
        while(!queue.isEmpty()){
            int node = queue.remove();
            seen.add(node);
            List<Integer> neiNodes = preMap.get(node);
            for(int neinode : neiNodes){
                if (indegree[neinode] - 1 == 0){
                    queue.add(neinode);
                }
                indegree[neinode] -= 1;
            }
        }
        return seen.size() == numCourses;

    }
}